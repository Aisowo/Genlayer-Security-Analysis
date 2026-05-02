from genlayer import Contract
import genlayer as gl

class GreetingContract(Contract):

    @gl.public
    def evaluate(self, input_text: str) -> str:
        if "hello" in input_text.lower():
            return "Greeting detected"
        return "No greeting detected"
