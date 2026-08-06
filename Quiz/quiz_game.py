class Quiz:
    def __init__(self, question: str, choices: list, answer: int):
        """
        개별 퀴즈 데이터를 담는 클래스
        
        :param question: 문제 텍스트
        :param choices: 4개의 선택지 리스트
        :param answer: 정답 번호 (1 ~ 4)
        """
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, index: int):
        """문제를 터미널에 포맷팅하여 출력합니다."""
        print(f"\nQ{index}. {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}) {choice}")

    def check_answer(self, user_input: int) -> bool:
        """사용자 입력과 정답 번호가 일치하는지 비교합니다."""
        return self.answer == user_input

    def to_dict(self) -> dict:
        """JSON 저장을 위한 딕셔너리 변환 메서드"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data: dict):
        """딕셔너리로부터 Quiz 객체를 복원하는 팩토리 메서드"""
        return cls(data["question"], data["choices"], data["answer"])
