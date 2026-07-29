"""Token-based rule chatbot with point-scoring answer selection."""

from itertools import zip_longest
from collections import defaultdict
import random
import re
import uuid


class Bot:
    id_list = set()
    
    def __init__(self, name):
        self.name = name
        self.query_tokens = dict()
        self.query_answers = dict()
        self.tk_pts = defaultdict(int)
        self.unknown_case = ["I don't understand this."]
        self.resistance = {"": ["Please write something.", "You didn't provide any query."]}
           
        while (id := random.randint(100, 500)) in Bot.id_list:
            pass
        self.id = id
        Bot.id_list.add(id)

    def tokenize(self, text: str) -> list:
        pattern = r"""
            \w+'\w+
            | \w+[-\w]+
            | \w+
            | [^\w\s]
            """
        tokens = re.findall(pattern, text, re.X)
        return tokens
        
    def add_tokens_answers(self, tokens: list, answers: list, tk_id: str = "") -> None:
        if not tk_id:
            tk_id = uuid.uuid4().hex[:7]
        if not isinstance(tk_id, str):
            raise TypeError("Token id should be a string.")
        self.query_tokens[tk_id] = set(tokens)
        self.query_answers[tk_id] = [answers] if isinstance(answers, str) else answers
    
    def add_unknown_case(self, unknown_case: list) -> None:
        self.unknown_case = unknown_case
    
    def add_resistance(self, tokens: list, answers: list) -> None:
        self.resistance[tuple(tokens)] = answers
        
    def answer(self, prompt_tokens: list) -> str:
        self.tk_pts.clear()
        for p_tk, res_tk in zip_longest(prompt_tokens, self.resistance.keys(), fillvalue=""):
            if not p_tk in res_tk:
                for id, tokens in self.query_tokens.items():
                    if p_tk in tokens:
                        self.tk_pts[id] += 1
            else:
                res_answer = random.choice(self.resistance[res_tk])
                return f"Bot: {res_answer}"
        if self.tk_pts:
            max_score = max(self.tk_pts.values())
            best_match_ids = [id for id, score in self.tk_pts.items() if score == max_score]
            choosed_id = random.choice(best_match_ids)
            answers = self.query_answers[choosed_id]
            choosed_asw = random.choice(answers)
            return f"Bot: {choosed_asw}"
        else:
            unknown = random.choice(self.unknown_case)
            return f"Bot: {unknown}"


def add_tokens_answers_to_bot(bot: Bot) -> None:
    query_tokens = [
        "hi, hello, hi, how, hey, !, good, morning, afternoon, evening, night".split(", "),
        "how, are, you, doing, what's, up, watsup?".split(", "),
        "i, am, good, fine, happy".split(", "),
        "i, am, bad, furious, unhappy".split(", "),
        "who, what, are, you, ?".split(", "),
        "what, can, you, do, service, serve, ?".split(", "),
        "what, is code, labs, company, ?".split(", "),
        "what, electronic, device, devices, products, i, could, get, buy".split(", "),
    ]
    query_answers = [
        "Greetings!",
        "I am fine, thanks. And you?",
        "Glad to hear that. How can I help you?",
        "I am sorry to hear that. What seems to be the problem?",
        "I am a bot here to serve you. How can I help you?",
        "I can get you in touch with a member of the company, or I can give you a list of products...",
        "We at Code Labs specialize in electronic devices.",
        "We have: Smartphones, Cameras, Radios, Speakers, and more...",
    ]
    unknown = ["I'm not sure how to respond to that. Can you rephrase?"]
    for tokens, answer in zip(query_tokens, query_answers):
        bot.add_tokens_answers(tokens, answer)
    bot.add_unknown_case(unknown)


def main():
    gptbot = Bot("gpt")
    add_tokens_answers_to_bot(gptbot)
    print("Bot: Hello! How can I assist you today?")
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye!")
            break
        prompt_tokens = gptbot.tokenize(prompt.lower())
        print(gptbot.answer(prompt_tokens))


if __name__ == "__main__":
    main()