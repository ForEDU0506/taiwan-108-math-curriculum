"""
國中數學二次方根：動態隨機題目生成引擎（Python 規範）
檔案名稱：題目生成引擎_隨機出題規格.py
功能說明：
1. 定義 8 大階段之「題目形式（Problem Templates / Schema）」。
2. 使用 Python 撰寫各階段題目的動態隨機參數生成演算法（保證數字漂亮、符合 108 課綱評量界線）。
3. 供 Gemini AI 教練作為「動態出題邏輯核心」，徹底擺脫固定死記題庫，實現無限動態隨機出題。
"""

import random
import math

# ==========================================
# 工具函式：數論輔助
# ==========================================
def get_square_free_factor(n):
    """分解 n = a^2 * b，回傳 (a, b)，其中 b 為無平方因數 (square-free)"""
    a = 1
    b = n
    for i in range(int(math.isqrt(n)), 1, -1):
        if n % (i * i) == 0:
            a = i
            b = n // (i * i)
            break
    return a, b

# ==========================================
# 階段 1：幾何引入與學習動機（建立數感與直觀）
# ==========================================
class Stage1Generator:
    """
    形式 1-A：正方形面積求邊長
    形式 1-B：邊長平方求面積
    """
    @staticmethod
    def generate():
        mode = random.choice(["1-A", "1-B"])
        if mode == "1-A":
            # 挑選非完全平方數面積 (2 ~ 35)
            non_squares = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 31]
            area = random.choice(non_squares)
            return {
                "stage": 1,
                "type": "1-A (面積求邊長)",
                "question": f"如果有一個正方形地毯，它的面積剛好是 {area} 平方公尺，請問它的邊長是多少公尺？",
                "target_answer": f"\\sqrt{{{area}}} 公尺",
                "hint_steps": [
                    "第一步：想一想正方形面積公式：邊長 × 邊長 = 面積。",
                    f"第二步：有沒有哪一個整數自己乘自己會剛好等於 {area}？",
                    f"第三步：既然無法用整數表示，數學家用什麼新符號來代表『面積為 {area} 的正方形邊長』？"
                ]
            }
        else:
            k = random.choice([3, 5, 6, 7, 11, 13, 15, 17])
            return {
                "stage": 1,
                "type": "1-B (根號平方的幾何直觀)",
                "question": f"計算 (\\sqrt{{{k}}})^2 與 \\sqrt{{{k}}} \\times \\sqrt{{{k}}} 的值。",
                "target_answer": f"{k}",
                "hint_steps": [
                    f"第一步：\\sqrt{{{k}}} 的幾何意義是什麼？（它是面積為多少的正方形邊長？）",
                    f"第二步：邊長 × 邊長 會還原成什麼？"
                ]
            }

# ==========================================
# 階段 2：符號定義與基本性質（觀念精確化）
# ==========================================
class Stage2Generator:
    """
    形式 2-A：辨析「k 的平方根」vs「\\sqrt{k}」
    形式 2-B：根號有意義的條件不等式
    形式 2-C：大小比較（整數 vs 根號）
    """
    @staticmethod
    def generate():
        mode = random.choice(["2-A", "2-B", "2-C"])
        if mode == "2-A":
            k = random.choice([4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144])
            sqrt_k = int(math.isqrt(k))
            sub_type = random.choice(["ask_roots", "ask_symbol"])
            if sub_type == "ask_roots":
                return {
                    "stage": 2,
                    "type": "2-A1 (某數的平方根)",
                    "question": f"請問 {k} 的平方根是多少？",
                    "target_answer": f"\\pm {sqrt_k}",
                    "hint_steps": [
                        f"第一步：思考『誰的平方會等於 {k}？』",
                        f"第二步：正數的平方根有幾個？（記得負數乘負數也是正數喔！）"
                    ]
                }
            else:
                return {
                    "stage": 2,
                    "type": "2-A2 (根號記號的本質)",
                    "question": f"計算 \\sqrt{{{k}}} 與 -\\sqrt{{{k}}} 的值分別是多少？",
                    "target_answer": f"\\sqrt{{{k}}} = {sqrt_k}，-\\sqrt{{{k}}} = -{sqrt_k}",
                    "hint_steps": [
                        "第一步：根號符號 \\sqrt{ } 本身專指『正平方根』還是『正負平方根』？",
                        "第二步：前面沒有負號時，答案只有正的那一個！"
                    ]
                }
        elif mode == "2-B":
            a = random.choice([2, 3, 4, 5])
            b = random.choice([6, 8, 10, 12, 15, 20])
            # ax - b >= 0 => x >= b/a
            g = math.gcd(b, a)
            simp_b = b // g
            simp_a = a // g
            ans_val = f"{simp_b}" if simp_a == 1 else f"\\frac{{{simp_b}}}{{{simp_a}}}"
            return {
                "stage": 2,
                "type": "2-B (根號有意義條件)",
                "question": f"若式子 \\sqrt{{{a}x - {b}}} 在實數範圍內有意義，求 x 的取值範圍。",
                "target_answer": f"x \\ge {ans_val}",
                "hint_steps": [
                    "第一步：在實數範圍內，任何數的平方都不可能是負數。",
                    "第二步：所以根號內部的值必須『大於或等於 0』。",
                    f"第三步：列出不等式：{a}x - {b} \\ge 0，移項後除以 x 的係數，並約分化為最簡分數。"
                ]
            }
        else: # 2-C 大小比較
            int_val = random.randint(3, 9)
            sq_val = int_val * int_val
            # 挑選 sq_val 附近的數
            offset = random.choice([-2, -1, 1, 2])
            target = sq_val + offset
            return {
                "stage": 2,
                "type": "2-C (大小比較)",
                "question": f"比較整數 {int_val} 與 \\sqrt{{{target}}} 的大小關係。",
                "target_answer": f"{int_val} > \\sqrt{{{target}}}" if sq_val > target else f"{int_val} < \\sqrt{{{target}}}",
                "hint_steps": [
                    f"第一步：把整數 {int_val} 換算回根號：{int_val} = \\sqrt{{{int_val}^2}} = \\sqrt{{{sq_val}}}。",
                    f"第二步：比較 \\sqrt{{{sq_val}}} 與 \\sqrt{{{target}}}，根號裡面數字愈大，邊長愈長。"
                ]
            }

# ==========================================
# 階段 3：完全平方數與根式化簡基本功
# ==========================================
class Stage3Generator:
    """
    形式 3-A：提出平方因數化為最簡根式 (如 \\sqrt{a^2 * b} = a\\sqrt{b})
    形式 3-B：乘上最小正整數 n 成為完全平方數
    """
    @staticmethod
    def generate():
        mode = random.choice(["3-A", "3-B"])
        if mode == "3-A":
            a = random.choice([2, 3, 4, 5, 6, 7])
            b = random.choice([2, 3, 5, 6, 7])
            n = (a * a) * b
            return {
                "stage": 3,
                "type": "3-A (提出平方因數)",
                "question": f"將 \\sqrt{{{n}}} 化為最簡根式。",
                "target_answer": f"{a}\\sqrt{{{b}}}",
                "hint_steps": [
                    f"第一步：對 {n} 進行質因數分解。",
                    f"第二步：檢查 {n} 裡面藏有哪一個完全平方數？（{n} = {a}^2 \\times {b}）。",
                    f"第三步：將平方數提出根號外面（\\sqrt{{{a}^2}} = {a}），留下未湊成對的數字在根號內。"
                ]
            }
        else: # 3-B 最小正整數 n
            a = random.choice([2, 3, 5])
            b = random.choice([2, 3, 5])
            while a == b:
                b = random.choice([2, 3, 5])
            base = (a * a * a) * b # a^3 * b => 至少需補一個 a 和一個 b
            req_n = a * b
            return {
                "stage": 3,
                "type": "3-B (配成完全平方數)",
                "question": f"若 \\sqrt{{{base} \\times n}} 為正整數，求正整數 n 的最小值。",
                "target_answer": f"{req_n}",
                "hint_steps": [
                    f"第一步：將 {base} 質因數分解。",
                    "第二步：要能夠完全開出根號，所有質因數的次方必須都是『偶數』。",
                    "第三步：找出哪幾個質因數的次方還是奇數？最少需要乘上誰把它們補齊成偶數？"
                ]
            }

# ==========================================
# 階段 4：數值估算與十分逼近法
# ==========================================
class Stage4Generator:
    """
    形式 4-A：夾擠法求整數範圍 (m < \\sqrt{N} < m+1)
    形式 4-B：整數部分與小數部分分離
    """
    @staticmethod
    def generate():
        m = random.randint(3, 15)
        # N 落在 m^2 + 1 到 (m+1)^2 - 1 之間
        low = m * m
        high = (m + 1) * (m + 1)
        N = random.randint(low + 1, high - 1)
        
        mode = random.choice(["4-A", "4-B"])
        if mode == "4-A":
            return {
                "stage": 4,
                "type": "4-A (夾擠求整數範圍)",
                "question": f"設 a 為正整數，若 a < \\sqrt{{{N}}} < a + 1，求 a 的值。",
                "target_answer": f"{m}",
                "hint_steps": [
                    f"第一步：找出 {N} 附近的完全平方數：{m}^2 = {low}，{m+1}^2 = {high}。",
                    f"第二步：因為 {low} < {N} < {high}，所以 \\sqrt{{{low}}} < \\sqrt{{{N}}} < \\sqrt{{{high}}}。",
                    f"第三步：得出連續整數範圍，即可找出 a。"
                ]
            }
        else: # 4-B 小數部分
            return {
                "stage": 4,
                "type": "4-B (小數部分表示法)",
                "question": f"已知 \\sqrt{{{N}}} 的整數部分為 x，小數部分為 y，求 x 與 y 的值。",
                "target_answer": f"x = {m}, y = \\sqrt{{{N}}} - {m}",
                "hint_steps": [
                    f"第一步：利用完全平方數夾擠，找出 {N} 介於哪兩個連續整數的平方之間，即可求出整數部分 x。",
                    "第二步：任何正數都由『整數部分』與『小數部分』組成。",
                    "第三步：將原數減去整數部分，即可用最簡根式表示出精確的小數部分 y。"
                ]
            }

# ==========================================
# 階段 5：根式的乘除法與單項式分母有理化
# ==========================================
class Stage5Generator:
    """
    形式 5-A：含係數乘法 (p\\sqrt{a})(q\\sqrt{b})
    形式 5-B：根號內除法約分
    形式 5-C：單項式分母有理化
    """
    @staticmethod
    def generate():
        mode = random.choice(["5-A", "5-B", "5-C"])
        if mode == "5-A":
            p = random.randint(2, 4)
            q = random.randint(2, 5)
            a = random.choice([2, 3, 5])
            b = random.choice([2, 3, 6, 10])
            prod_inner = a * b
            sim_p, sim_inner = get_square_free_factor(prod_inner)
            final_coeff = p * q * sim_p
            ans = f"{final_coeff}\\sqrt{{{sim_inner}}}" if sim_inner > 1 else f"{final_coeff}"
            return {
                "stage": 5,
                "type": "5-A (根式乘法)",
                "question": f"計算 ({p}\\sqrt{{{a}}}) \\times ({q}\\sqrt{{{b}}})，並化為最簡根式。",
                "target_answer": ans,
                "hint_steps": [
                    f"第一步：外乘外、內乘內：({p} \\times {q})\\sqrt{{{a} \\times {b}}} = {p*q}\\sqrt{{{prod_inner}}}。",
                    f"第二步：檢查根號內的 {prod_inner} 是否還能提出完全平方因數化簡？"
                ]
            }
        elif mode == "5-B":
            b = random.choice([2, 3, 5, 6])
            quotient = random.choice([4, 9, 16, 25])
            a = b * quotient
            return {
                "stage": 5,
                "type": "5-B (根式除法與直接約分)",
                "question": f"計算 \\frac{{\\sqrt{{{a}}}}}{{\\sqrt{{{b}}}}} 之值。",
                "target_answer": f"{int(math.isqrt(quotient))}",
                "hint_steps": [
                    f"第一步：利用除法法則，合併到同一個根號內：\\sqrt{{\\frac{{{a}}}{{{b}}}}}。",
                    f"第二步：在根號內直接約分，計算 {a} \\div {b} 是多少？",
                    "第三步：開出完全平方數。"
                ]
            }
        else: # 5-C 單項式分母有理化
            denom_inner = random.choice([2, 3, 5, 7])
            numer = denom_inner * random.randint(2, 4) # 能整除約分
            ans_coeff = numer // denom_inner
            return {
                "stage": 5,
                "type": "5-C (單項分母有理化)",
                "question": f"將 \\frac{{{numer}}}{{\\sqrt{{{denom_inner}}}}} 分母有理化，並化為最簡根式。",
                "target_answer": f"{ans_coeff}\\sqrt{{{denom_inner}}}",
                "hint_steps": [
                    f"第一步：擴分！分子與分母同時乘以分母的根號 \\sqrt{{{denom_inner}}}。",
                    f"第二步：分母變成 \\sqrt{{{denom_inner}}} \\times \\sqrt{{{denom_inner}}} = {denom_inner}。",
                    f"第三步：分子是 {numer}\\sqrt{{{denom_inner}}}，檢查外面的 {numer} 與分母 {denom_inner} 能否約分。"
                ]
            }

# ==========================================
# 階段 6：同類根式與加減運算
# ==========================================
class Stage6Generator:
    """
    形式 6-A：先化簡後合併的多項根式加減
    """
    @staticmethod
    def generate():
        base_inner = random.choice([2, 3, 5])
        # 確保 c1 + c2 != c3，防止係數相抵消出現 0\sqrt{base} 錯誤
        c1, c2, c3 = random.sample([2, 3, 4, 5], 3)
        while c1 + c2 == c3:
            c1, c2, c3 = random.sample([2, 3, 4, 5], 3)
            
        n1 = c1 * c1 * base_inner
        n2 = c2 * c2 * base_inner
        n3 = c3 * c3 * base_inner
        
        final_coeff = c1 + c2 - c3
        if final_coeff == 1:
            ans = f"\\sqrt{{{base_inner}}}"
        elif final_coeff == -1:
            ans = f"-\\sqrt{{{base_inner}}}"
        else:
            ans = f"{final_coeff}\\sqrt{{{base_inner}}}"
        
        return {
            "stage": 6,
            "type": "6-A (同類根式先化簡後合併)",
            "question": f"計算 \\sqrt{{{n1}}} + \\sqrt{{{n2}}} - \\sqrt{{{n3}}} 之值。",
            "target_answer": ans,
            "hint_steps": [
                "第一步（各自化簡）：分別將這三個根式提出根號內的完全平方因數，化為最簡根式。",
                f"第二步：觀察化簡後的各項，確認根號內部是否都是 \\sqrt{{{base_inner}}}（確認為同類根式）。",
                "第三步：將同類根式外面的整數係數進行加減運算合併。"
            ]
        }

# ==========================================
# 階段 7：乘法公式應用與雙項式分母有理化
# ==========================================
class Stage7Generator:
    """
    形式 7-A：平方差公式展開 (\\sqrt{a} + \\sqrt{b})(\\sqrt{a} - \\sqrt{b})
    形式 7-B：和平方 / 差平方公式
    形式 7-C：雙項式平方差配對分母有理化（🌟 依 D022 決議：預設不出，僅供選讀挑戰）
    """
    @staticmethod
    def generate(include_advanced: bool = False):
        # 遵循 D022 決議：預設僅從課綱核心題型 7-A 與 7-B 出題，雙項有理化僅保留為選讀挑戰
        mode = random.choice(["7-A", "7-B", "7-C"]) if include_advanced else random.choice(["7-A", "7-B"])
        if mode == "7-A":
            a = random.choice([5, 6, 7, 10])
            b = random.choice([2, 3])
            ans = a - b
            return {
                "stage": 7,
                "type": "7-A (平方差公式消根號)",
                "question": f"計算 (\\sqrt{{{a}}} + \\sqrt{{{b}}})(\\sqrt{{{a}}} - \\sqrt{{{b}}}) 之值。",
                "target_answer": f"{ans}",
                "hint_steps": [
                    "第一步：觀察括號結構，這是乘法公式中的平方差結構：(A + B)(A - B) = A^2 - B^2。",
                    f"第二步：根號平方會還原成有理數：(\\sqrt{{{a}}})^2 與 (\\sqrt{{{b}}})^2 分別是多少？",
                    "第三步：計算兩數相減，得到整數結果。"
                ]
            }
        elif mode == "7-B":
            sign = random.choice(["+", "-"])
            a = random.choice([3, 5, 7])
            b = random.choice([2, 3])
            while a == b: b = random.choice([2, 5])
            prod = a * b
            const_term = a + b
            cross_sign = "+" if sign == "+" else "-"
            ans = f"{const_term} {cross_sign} 2\\sqrt{{{prod}}}"
            return {
                "stage": 7,
                "type": "7-B (和差平方公式展開)",
                "question": f"計算 (\\sqrt{{{a}}} {sign} \\sqrt{{{b}}})^2 之值。",
                "target_answer": ans,
                "hint_steps": [
                    f"第一步：套用乘法公式：(A {sign} B)^2 = A^2 {cross_sign} 2AB + B^2。",
                    "第二步：計算首項平方與末項平方，相加得出常數部分。",
                    f"第三步：計算中間交叉項（兩數相乘再乘以 2），注意中間運算符號為『{cross_sign}』。"
                ]
            }
        else: # 7-C 雙項有理化（選讀挑戰）
            a = random.choice([3, 5, 6])
            b = a - 1 # 分母為 1 簡化運算
            # 1 / (\sqrt{a} - \sqrt{b}) => \sqrt{a} + \sqrt{b}
            return {
                "stage": 7,
                "type": "7-C (🌟 選讀挑戰：雙項式分母有理化)",
                "question": f"將 \\frac{{1}}{{\\sqrt{{{a}}} - \\sqrt{{{b}}}}} 分母有理化。",
                "target_answer": f"\\sqrt{{{a}}} + \\sqrt{{{b}}}",
                "hint_steps": [
                    f"第一步：觀察分母，找出能利用平方差公式消除根號的配對式 (\\sqrt{{{a}}} + \\sqrt{{{b}}})。",
                    f"第二步：分子與分母同時乘以該式進行擴分，計算分母平方差 (\\sqrt{{{a}}})^2 - (\\sqrt{{{b}}})^2 的值。",
                    "第三步：化簡分子並檢驗是否能與分母約分。"
                ]
            }

# ==========================================
# 階段 8：綜合應用與評量界線
# ==========================================
class Stage8Generator:
    """
    形式 8-A：含根式係數之一元一次方程式
    形式 8-B：畢氏定理直角三角形斜邊計算
    """
    @staticmethod
    def generate():
        mode = random.choice(["8-A", "8-B"])
        if mode == "8-A":
            k = random.choice([2, 3, 5])
            multiplier = random.randint(2, 5)
            right = multiplier * k
            # \sqrt{k} x = right => x = right / \sqrt{k} = multiplier \sqrt{k}
            return {
                "stage": 8,
                "type": "8-A (根式係數一元一次方程式)",
                "question": f"解一元一次方程式：\\sqrt{{{k}}} x = {right}。",
                "target_answer": f"x = {multiplier}\\sqrt{{{k}}}",
                "hint_steps": [
                    f"第一步：利用等量公理，方程式兩邊同除以未知數的係數 \\sqrt{{{k}}}。",
                    f"第二步：進行分母有理化，分子與分母同時乘以 \\sqrt{{{k}}}。",
                    "第三步：將整數部分約分，求出最簡根式解。"
                ]
            }
        else: # 8-B 畢氏定理
            a = random.randint(2, 6)
            b = random.randint(2, 5)
            c_sq = a * a + b * b
            simp_a, simp_b = get_square_free_factor(c_sq)
            ans = f"{simp_a}\\sqrt{{{simp_b}}}" if simp_a > 1 and simp_b > 1 else (f"{simp_a}" if simp_b == 1 else f"\\sqrt{{{c_sq}}}")
            return {
                "stage": 8,
                "type": "8-B (畢氏定理幾何應用)",
                "question": f"直角三角形的兩股長分別為 {a} 與 {b}，求斜邊長。",
                "target_answer": ans,
                "hint_steps": [
                    "第一步：依據畢氏定理，直角三角形中斜邊長度的平方等於兩股長度的平方和。",
                    "第二步：分別計算兩股的平方，並相加得出斜邊平方之值。",
                    "第三步：對該數開根號，並提出完全平方因數化為最簡根式。"
                ]
            }

# ==========================================
# 總調度分發器
# ==========================================
STAGE_GENERATORS = {
    1: Stage1Generator,
    2: Stage2Generator,
    3: Stage3Generator,
    4: Stage4Generator,
    5: Stage5Generator,
    6: Stage6Generator,
    7: Stage7Generator,
    8: Stage8Generator,
}

def generate_random_question(stage_num: int, include_advanced: bool = False):
    """為指定階段產生一道隨機題目"""
    gen = STAGE_GENERATORS.get(stage_num, Stage1Generator)
    if stage_num == 7:
        return gen.generate(include_advanced=include_advanced)
    return gen.generate()

if __name__ == "__main__":
    print("=== 測試 8 大階段隨機題目生成結果 ===")
    for s in range(1, 9):
        q = generate_random_question(s)
        print(f"\n[階段 {q['stage']} - {q['type']}]")
        print(f"題目：{q['question']}")
        print(f"目標解答：{q['target_answer']}")
        print("思考階梯：")
        for h in q['hint_steps']:
            print(f"  {h}")
