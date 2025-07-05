# 짝 홀 구분될 리스트 선언
A = []
B = []

# 스택 정수 원소들 리스트로 받기
while True:
    try:
        stack = list(map(int, input("스택 정수 원소들 입력: ").split()))
        print("입력된 스택:", stack)
        break
    
    # 예외처리 (정수가 아님)
    except ValueError:
        print("잘못된 입력입니다. 정수만 입력해주세요.")
        stack = []

# 원소들의 짝 홀 구분으로 스택 A, B 나누기
for i in range(len(stack)):
    if stack[i] %2 == 0:
        A.append(stack[i])
    else :
        B.append(stack[i])
        
print(A)
print(B)

# 스택 명령어 class 정의
class stack_Manager :
    def __init__(self, steak_A, steak_B):
        self.steak_A = steak_A
        self.steak_B = steak_B
    
    # 추가 (예외처리 완료)
    def adds(self):
        try :
            element = []
            element = list(map(int, input("추가할 원소 입력: ").split()))
            print(element)
            for i in range(len(element)):
                if element[i] %2 == 0:
                    A.append(element[i])
                else :
                    B.append(element[i])
                    
            print(A)
            print(B)
            
        except ValueError :
            print("정수만 입력하세요")
            element = []
            manager.adds()
        
    # 삭제 (예외처리 완료)
    def removes(self):
        prompt = list(input("제거할 스택과 수량 입력(예시 : A 4) : ").split())
        if len(prompt) > 2 :
            print("잘못된 입력입니다ㅑ")
            return
                
            
        print(prompt[0])
        print(prompt[1])
        
        count = int(prompt[1])
        if prompt[0] == "A" :
            del A[-count:]
            
        elif prompt[0] == "B" :
            del B[-count:]
        print(A)
        print(B)
        
    # 수정 (제작 미정)
    def correction (self):
        while True:
            try : 
                cor_element = int(input("수정할 원소 입력:"))
                print("입력한 원소 : " , cor_element)
                break
            except ValueError:
                print("정수를 입력해주세요")
                cor_element = None
                
        if cor_element in A:
            
            pass
        
    # 출력 (예외 필요X)
    def prints (self):
        print(A)
        print(B)
        
    # 종료 (예외 필요X)
    def ends ():
        print("프로젝트를 종료합니다")
        exit()

# 스택 명령어 대기
manager = stack_Manager(A, B)

# 스택 명령어 입력
while True : 
    print("명령을 입력하세요")
    other = input(" adds  removes  prints  ends  ")
    
    if other == "adds" :
        stack_Manager.adds()
        other = None
        
    elif other == "removes" :
        stack_Manager.removes()
        other = None
        
    # hiden
    elif other == "correction" :
        stack_Manager.correction()
        other = None
        
    elif other == "ends" :
        stack_Manager.ends()
        other = None
        
    elif other == "prints" :
        stack_Manager.prints()
        other = None
        
    else :
        print("다시 입력해주세요")
        continue