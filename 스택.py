class StackManager:
    def __init__(self, name):
        self.name = name
        self.odd = []
        self.even = []

    # 추가 (예외처리 완료)
    def adds(self):
        try:
            add_element = list(map(int, input("추가할 원소 입력: ").split()))
            for num in add_element:
                if num % 2 == 0:
                    self.even.append(num)
                else:
                    self.odd.append(num)
            print("현재 짝수 스택:", self.even)
            print("현재 홀수 스택:", self.odd)
        except ValueError:
            print("정수만 입력하세요")
            self.adds()

    # 삭제 (예외처리 완료)
    def removes(self):
        remove_element = input("제거할 스택과 수량 입력(예시: even 4): ").split()
        if len(remove_element) != 2 or remove_element[0] not in ["even", "odd"]:
            print("잘못된 입력입니다")
            return
        try:
            count = int(remove_element[1])
        except ValueError:
            print("수량은 정수로 입력하세요")
            return
        if remove_element[0] == "even":
            del self.even[-count:]
        else:
            del self.odd[-count:]
        print("현재 짝수 스택:", self.even)
        print("현재 홀수 스택:", self.odd)

    # 출력
    def prints(self):
        print("짝수 스택:", self.even)
        print("홀수 스택:", self.odd)

    # 종료
    def ends(self):
        print("프로그램을 종료합니다.")
        exit()

# 스택 저장할 딕셔너리
stack_dict = {}

while True:
    print("명령을 입력하세요")
    print("예시: name adds / new name / name removes / name prints / ends")
    command = input(">>> ").split()
    
    if not command:
        continue

    if command[0] == "new":
        if len(command) < 2:
            print("스택 이름을 입력하세요.")
            continue
        name = command[1]
        if name in stack_dict:
            print(f"이미 '{name}' 스택이 존재합니다.")
        else:
            stack_dict[name] = StackManager(name)
            print(f"'{name}' 스택이 생성되었습니다.")

    elif command[0] == "ends":
        print("프로그램을 종료합니다.")
        break

    elif command[0] == "list":
        if not stack_dict:
            print("아직 생성된 스택이 없습니다.")
        else:
            print("현재 생성된 스택들:", ", ".join(stack_dict.keys()))

    elif len(command) >= 2:
        name = command[0]
        action = command[1]

        if name not in stack_dict:
            print(f"스택 '{name}' 이 존재하지 않습니다.")
            continue

        stack = stack_dict[name]

        if action == "adds":
            stack.adds()
        elif action == "removes":
            stack.removes()
        elif action == "prints":
            stack.prints()
        else:
            print("지원되지 않는 명령입니다.")
    else:
        print("잘못된 명령입니다. 다시 시도해주세요.")