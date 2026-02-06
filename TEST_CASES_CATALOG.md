# TyC Parser Test Cases Catalog

Tài liệu này liệt kê chi tiết các kịch bản kiểm thử cho bộ phân tích cú pháp (Parser) của ngôn ngữ TyC. Mục tiêu là bao phủ từ cú pháp cơ bản đến các trường hợp biên, lắt léo và dễ gây lỗi.

## 1. Cấu trúc Chương trình (Program Structure)
Kiểm tra khả năng parse tổng thể của một file mã nguồn.

### Standard Cases
*   [x] File rỗng.
*   [x] File chỉ chứa comment hoặc khoảng trắng.
*   [x] Chương trình chỉ có hàm `main`.
*   [x] Chương trình có khai báo struct và hàm đan xen.

### Hard/Hidden Cases
*   [ ] **No Main**: File hợp lệ về cú pháp nhưng không có hàm main (Parser vẫn nên chấp nhận, Semantic mới báo lỗi).
*   [ ] **Trailing Trash**: File hợp lệ nhưng có ký tự rác sau dấu `}` cuối cùng của hàm main.
*   [ ] **EOF handling**: Kết thúc file đột ngột ngay sau một token khóa.
*   [ ] **Large File**: File chứa hàng nghìn dòng code (xem stack overflow của parser đệ quy).

---

## 2. Khai báo Struct (Struct Declaration)
Cú pháp: `struct Name { Type field; ... };`

### Standard Cases
*   [x] Struct rỗng: `struct Empty {};`.
*   [x] Struct 1 field.
*   [x] Struct nhiều field cùng kiểu/khác kiểu.

### Hard/Hidden Cases
*   [ ] **Nested Struct Definition**: Định nghĩa struct lồng trong struct (Thường bị cấm: `struct A { struct B { ... }; };`).
*   [ ] **Self-Reference**: Struct chứa field là chính nó (Gây lỗi vô hạn kích thước nếu không dùng con trỏ - TyC đơn giản có thể cấm).
*   [ ] **Keyword Naming**: Tên struct hoặc tên field trùng với keyword (`struct if { ... }` -> Error).
*   [ ] **Missing Semicolon**: Thiếu dấu chấm phẩy sau dấu ngoặc nhọn đóng `};`.
*   [ ] **Anonymous Struct**: `struct { int x; } p;` (Nếu ngôn ngữ hỗ trợ).

---

## 3. Khai báo Hàm (Function Declaration)
Cú pháp: `ReturnType Name(Params) { Body }`

### Standard Cases
*   [x] Hàm void không tham số.
*   [x] Hàm có trả về (int, float, string, struct).
*   [x] Hàm 1 tham số, nhiều tham số.
*   [x] Hàm trả về struct.

### Hard/Hidden Cases
*   [ ] **Empty Body**: `void func() {}` (Hợp lệ).
*   [ ] **Missing Body**: `void func();` (Nếu không hỗ trợ forward declaration thì là lỗi).
*   [ ] **Parameter Shadowing**: Tên tham số trùng tên hàm.
*   [ ] **Array/Struct Parameters**: Tham số là struct phức tạp.
*   [ ] **Conflict Return**: Khai báo `int` nhưng không `return` hoặc `return` sai kiểu (Parser thường cho qua, Semantic bắt lỗi).
*   [ ] **Auto Parameter**: Dùng `auto` cho tham số `void f(auto x)` (Thường là lỗi trong C-like đơn giản).

---

## 4. Khai báo Biến (Variable Declaration)
Cú pháp: `Type name` hoặc `Type name = expr;`

### Standard Cases
*   [x] Khai báo cơ bản: `int x;`, `float y;`.
*   [x] Khởi tạo giá trị: `int x = 10;`.
*   [x] Type Inference: `auto x = 10;`.
*   [x] Khai báo nhiều biến: `int x, y, z;` (Nếu hỗ trợ).

### Hard/Hidden Cases
*   [ ] **Chained Assignment**: `int x = y = z = 5;`.
*   [ ] **Complex Init**: `int x = (1 + 2) * func();`.
*   [ ] **Auto without Init**: `auto x;` (Lỗi, không suy diễn được kiểu).
*   [ ] **Reserved Word**: `int auto = 5;` (Lỗi).
*   [ ] **Void Variable**: `void x;` (Lỗi).
*   [ ] **Scope Shadowing**: Khai báo biến trùng tên trong block con `{ int x; { int x; } }`.

---

## 5. Câu lệnh Điều kiện (If Statement)

### Standard Cases
*   [x] If đơn giản.
*   [x] If - Else.
*   [x] Nested If.

### Hard/Hidden Cases
*   [ ] **Dangling Else**: `if (a) if (b) s1; else s2;` (Else thuộc về if gần nhất - if(b)).
*   [ ] **Empty Condition**: `if ()` (Lỗi).
*   [ ] **Assignment inside If**: `if (x = 5)` (Hợp lệ về cú pháp, nhưng là bad practice hoặc lỗi logic).
*   [ ] **Blockless Body**: `if (a) int x = 5;` (Một số ngôn ngữ cấm khai báo biến ngay sau if mà không có block `{}`).
*   [ ] **Multiple Elses**: `if ... else ... else ...` (Lỗi cú pháp).

---

## 6. Vòng lặp For (For Loop)
Cú pháp: `for (init; cond; step) body`

### Standard Cases
*   [x] Full parts: `for(int i=0; i<10; i++) {}`.
*   [x] Empty parts: `for(;;) {}`.
*   [x] Nested for.

### Hard/Hidden Cases
*   [ ] **Complex Init**: `for(int i=0, j=0; i<10; i++, j--)` (Nhiều biến, nhiều update).
*   [ ] **Scope of Init**: Truy cập biến `i` bên ngoài vòng for khi `i` được khai báo trong `init`.
*   [ ] **Variable Declaration in Body**: `for(...) int x = 5;` (Tương tự If, không có block).
*   [ ] **Break/Continue misplaced**: `break` nằm ngoài vòng lặp (Semantic check, nhưng Parser có thể check ngữ cảnh).

---

## 7. Vòng lặp While (While Loop)

### Standard Cases
*   [x] While cơ bản.
*   [x] While lồng nhau.
*   [x] While(true) / While(1).

### Hard/Hidden Cases
*   [ ] **Empty Body**: `while(cond);` (Vòng lặp rỗng, cẩn thận parser đòi hỏi `{}`).
*   [ ] **Assignment Condition**: `while(line = readLine())`.
*   [ ] **Do-While Confusion**: Viết nhầm `do { } while (cond)` nếu ngôn ngữ không hỗ trợ `do-while`.

---

## 8. Biểu thức (Expressions) & Operator Precedence
Đây là phần khó nhất của Parser.

### Standard Cases
*   [x] Số học: `+, -, *, /, %`.
*   [x] So sánh: `>, <, >=, <=, ==, !=`.
*   [x] Logic: `&&, ||, !`.
*   [x] Ngoặc đơn `()`.

### Hard/Hidden Cases
*   [ ] **Precedence Hell**: `a || b && c | d ^ e & f == g > h + i * j`. (Kiểm tra xem cây AST có đúng thứ tự ưu tiên không).
*   [ ] **Right Associativity**: `a = b = c = 5` (Phải gán từ phải qua trái).
*   [ ] **Unary Combinations**: `x = - - -5;` hay `x = ! ! y;` hay `x = + - + 5`.
*   [ ] **Function Call Priority**: `func(a) + 5` vs `func(a + 5)`.
*   [ ] **Member Access**: `p.x.y` (Truy cập lồng).
*   [ ] **Array/Index Access** (Nếu có): `a[i][j]`.
*   [ ] **Postfix/Prefix**: `++i` vs `i++` trong biểu thức phức tạp `a = i++ + ++j`.

---

## 9. Khác (Others)

### Standard Cases
*   [x] Return statement.
*   [x] Break/Continue.

### Hard/Hidden Cases
*   [ ] **Unreachable Code**: Code sau `return` hoặc `break` trong cùng block.
*   [ ] **Comment Tricky**: `int a = 5; // comment \n int b = 6;` (Đảm bảo parser không nuốt mất dòng sau).
*   [ ] **String Literals**: Chuỗi chứa ký tự đặc biệt, escape characters `\n, \t, \"`.
*   [ ] **Unclosed String/Comment**: Xử lý lỗi khi EOF gặp giữa chừng.

---

## Tổng kết Checklist
Để parser đạt điểm tối đa và robust, bạn cần đặc biệt chú ý vào mục **Expressions (Precedence)** và **Nested Structures** (If/Else, Loops). Hầu hết các lỗi compiler nằm ở việc xử lý sai độ ưu tiên toán tử hoặc nhập nhằng (ambiguity) trong ngữ pháp (như Dangling Else).
