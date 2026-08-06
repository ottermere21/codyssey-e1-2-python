import json
import os
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
        # 실행 디렉터리에 관계없이 항상 프로젝트 루트에 state.json이 생성되도록 경로 구성
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        self.filepath = os.path.join(project_root, filepath)
        
        self.quizzes = []
        self.best_score = 0
        self.load_data()

    def get_default_quizzes(self) -> list:
        """기본 반려동물 상식 퀴즈 데이터셋 반환"""
        return [
            {
                "question": "개의 땀샘은 주로 어느 신체 부위에 분포되어 있을까요?",
                "choices": ["귀 안쪽", "발바닥 패드", "코 끝", "등 피부"],
                "answer": 2
            },
            {
                "question": "고양이가 기분이 좋을 때 내는 기계음 같은 소리를 무엇이라고 할까요?",
                "choices": ["하악질", "골골송 (프르릉)", "야옹", "하품"],
                "answer": 2
            },
            {
                "question": "토끼의 이빨은 평생 동안 계속 자란다.",
                "choices": ["참, 평생 자란다", "거짓, 일정 시기에 멈춘다", "나이가 들면 빠진다", "알 수 없다"],
                "answer": 1
            },
            {
                "question": "앵무새가 사람의 말을 흉내 낼 수 있는 신체적 비결은 무엇일까요?",
                "choices": ["이빨이 없어서", "두껍고 유연한 혀와 명관", "사람과 동일한 성대", "발달한 청각"],
                "answer": 2
            },
            {
                "question": "햄스터의 볼주머니는 주로 어떤 용도로 사용될까요?",
                "choices": ["체온 조절", "음식 운반 및 임시 저장", "의사 소통", "물놀이 시 튜브 역할"],
                "answer": 2
            }
        ]

    def load_data(self):
        """JSON 상태 파일 로딩 및 유효성 검사, 예외 복구 수행"""
        if not os.path.exists(self.filepath):
            print("데이터 파일이 존재하지 않아 기본 데이터로 새로 생성합니다.")
            self.init_default_data()
            return

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)
                self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
        except (json.JSONDecodeError, KeyError, PermissionError) as e:
            print(f"\n⚠️ 경고: 데이터 파일({self.filepath})이 손상되었거나 읽을 수 없습니다.")
            print("안전한 실행을 위해 기본 데이터로 복구(초기화)를 진행합니다.")
            self.init_default_data()

    def init_default_data(self):
        """기본 상태 데이터로 초기화 후 자동 저장"""
        self.best_score = 0
        self.quizzes = [Quiz.from_dict(q) for q in self.get_default_quizzes()]
        self.save_data()

    def save_data(self):
        """현재 게임 상태를 JSON 파일로 저장"""
        try:
            data = {
                "best_score": self.best_score,
                "quizzes": [q.to_dict() for q in self.quizzes]
            }
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"⚠️ 파일 저장 중 오류가 발생했습니다: {e}")

    def play_quiz(self):
        print("\n[퀴즈 풀기] 기능은 현재 개발 중입니다.")

    def add_quiz(self):
        """새로운 퀴즈 추가"""
        print("\n=== 새 퀴즈 추가 ===")
        
        # 1. 문제 입력 받기
        question = input_with_validation("문제 질문을 입력하세요: ", str)
        
        # 2. 선택지 4개 입력 받기
        choices = []
        for i in range(1, 5):
            choice = input_with_validation(f"선택지 {i}번을 입력하세요: ", str)
            choices.append(choice)
            
        # 3. 정답 입력 받기 (1~4 범위 검사)
        answer = input_with_validation("정답 번호를 입력하세요 (1~4): ", int, (1, 4))
        
        # 4. Quiz 인스턴스 생성 및 리스트 추가
        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        
        # 5. 저장
        self.save_data()
        print("\n🎉 새로운 퀴즈가 성공적으로 추가되었습니다!")

    def view_quizzes(self):
        """저장된 전체 퀴즈 목록 출력"""
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해 주세요.")
            return

        print(f"\n=== 등록된 퀴즈 목록 (총 {len(self.quizzes)}개) ===")
        for i, q in enumerate(self.quizzes, 1):
            q.display(i)
            print(f"  👉 정답: {q.answer}번")

    def view_best_score(self):
        """최고 점수 확인"""
        print("\n=== 최고 점수 확인 ===")
        if self.best_score == 0:
            print("아직 퀴즈를 풀지 않았거나 기록이 없습니다. 첫 퀴즈에 도전해 보세요! (현재 최고 점수: 0점)")
        else:
            print(f"🏆 현재 기록된 최고 점수: {self.best_score}점")

    def run(self):
        """메인 메뉴 루프 실행 (강제 종료 예외 처리 포함)"""
        try:
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
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 사용자에 의해 프로그램이 강제 중단되었습니다.")
            print("진행 사항을 안전하게 저장하고 종료합니다.")
            self.save_data()


