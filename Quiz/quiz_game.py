from utils import input_with_validation

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


class QuizGame:
    def __init__(self, filepath: str = "state.json"):
        self.filepath = filepath
        self.quizzes = []
        self.best_score = 0

    def play_quiz(self):
        print("\n[퀴즈 풀기] 기능은 현재 개발 중입니다.")

    def add_quiz(self):
        print("\n[퀴즈 추가] 기능은 현재 개발 중입니다.")

    def view_quizzes(self):
        print("\n[퀴즈 목록 보기] 기능은 현재 개발 중입니다.")

    def view_best_score(self):
        print("\n[최고 점수 확인] 기능은 현재 개발 중입니다.")

    def run(self):
        """메인 메뉴 루프 실행"""
        while True:
            print("\n=== 반려동물 상식 퀴즈 게임 ===")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록 보기")
            print("4. 최고 점수 확인")
            print("5. 종료")
            
            # 1~5 범위의 메뉴 입력 검증 수행
            choice = input_with_validation("메뉴를 선택하세요: ", int, (1, 5))
            
            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.view_quizzes()
            elif choice == 4:
                self.view_best_score()
            elif choice == 5:
                print("프로그램을 종료합니다. 감사합니다!")
                break

