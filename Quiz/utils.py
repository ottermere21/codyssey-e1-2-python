def input_with_validation(prompt: str, input_type=int, val_range: tuple = None):
    """
    공백 제거, 예외 처리, 범위 검사가 반영된 입력 헬퍼 함수
    
    :param prompt: 입력 안내 메시지
    :param input_type: 기대하는 타입 (int 또는 str)
    :param val_range: (최소값, 최대값) 형태의 정수 튜플 (input_type이 int일 때만 유효)
    """
    while True:
        try:
            raw_input = input(prompt)
            # 1. 입력 앞뒤 공백 제거
            cleaned_input = raw_input.strip()
            
            # 2. 빈 입력 예외 처리
            if not cleaned_input:
                print("⚠️ 빈 입력은 허용되지 않습니다. 다시 입력해주세요.\n")
                continue

            # 3. 타입 변환 검사
            converted_value = input_type(cleaned_input)
            
            # 4. 정수 범위 검사
            if (input_type is int) and (val_range is not None):
                min_val, max_val = val_range
                if not (min_val <= converted_value <= max_val):
                    print(f"⚠️ 입력 범위를 벗어났습니다. ({min_val} ~ {max_val} 사이의 숫자를 입력해주세요.)\n")
                    continue
                    
            return converted_value

        except ValueError:
            # int 타입이고, 정수 범위를 벗어난 경우
            if input_type is int:
                print("⚠️ 유효한 숫자를 입력해 주세요. (예: 1, 2, 3)\n")
            # 그 외의 경우 (타입 변환 실패)
            else: 
                print("⚠️ 입력 형식이 올바르지 않습니다. 다시 시도해 주세요.\n")
            continue
