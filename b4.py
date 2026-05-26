# C1: Phân tích Input / Output
# - order_list là list chứa các đơn hàng và trạng thái.
# - choice là dữ liệu người dùng nhập để chọn menu chính.
# - sub_choice là dữ liệu chọn menu con cập nhật đơn hàng.
# - position là vị trí đơn hàng người dùng nhập vào.
# - order_code và order_status là dữ liệu nhập để thêm/sửa đơn hàng.
#
# - Output:
#   + Hiển thị danh sách đơn hàng.
#   + Thêm, sửa, xóa đơn hàng thành công.
#   + Thống kê số lượng đơn theo trạng thái.
#   + Thông báo lỗi nếu nhập sai dữ liệu hoặc sai vị trí.


# C2: Đề xuất giải pháp
# - Dùng while True để tạo menu chạy liên tục.
# - Dùng list để lưu danh sách đơn hàng.
# - Dùng input() để nhận dữ liệu từ người dùng.
# - Dùng strip() để xóa khoảng trắng thừa.
# - Dùng upper() để chuẩn hóa mã đơn và trạng thái.
# - Dùng append() để thêm đơn hàng mới.
# - Dùng phép gán qua index để cập nhật đơn hàng.
# - Dùng pop(index) để xóa đơn hàng theo vị trí.
# - Dùng isdigit() để kiểm tra dữ liệu nhập là số.
# - Dùng range() và len(order_list) để kiểm tra vị trí hợp lệ.
# - Dùng enumerate() để hiển thị danh sách có đánh số.
# - Dùng vòng lặp for để thống kê trạng thái đơn hàng.


# C3: Thiết kế thuật toán / Mô tả luồng chương trình
# B1: Khởi tạo danh sách order_list.
# B2: Hiển thị menu chính bằng while True.
# B3: Người dùng nhập choice.
# B4: Nếu choice không hợp lệ:
#       - In thông báo lỗi
#       - Quay lại menu
# B5: Nếu chọn 1:
#       - Kiểm tra danh sách rỗng
#       - Nếu có dữ liệu -> in danh sách đơn hàng
# B6: Nếu chọn 2:
#       - Hiển thị menu cập nhật
#       - Nhập sub_choice
# B7: Nếu sub_choice = 1:
#       - Nhập mã đơn và trạng thái
#       - Chuẩn hóa dữ liệu
#       - append() thêm vào danh sách
# B8: Nếu sub_choice = 2:
#       - Nhập vị trí cần sửa
#       - Kiểm tra vị trí hợp lệ
#       - Nhập dữ liệu mới
#       - Cập nhật bằng order_list[index]
# B9: Nếu sub_choice = 3:
#       - Nhập vị trí cần xóa
#       - Kiểm tra vị trí hợp lệ
#       - Xóa bằng pop(index)
#       - Hiển thị đơn vừa xóa
# B10: Nếu sub_choice = 4:
#       - Quay lại menu chính
# B11: Nếu chọn 3:
#       - Duyệt danh sách đơn hàng
#       - Đếm số lượng theo từng trạng thái
#       - In kết quả thống kê
# B12: Nếu chọn 4:
#       - In thông báo thoát
#       - break kết thúc chương trình
order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

valid_status = ["PENDING", "DELIVERING", "COMPLETED", "CANCELLED"]


def display_orders():
    if not order_list:
        print("Danh sách đơn hàng hiện đang trống.")
    else:
        print("\nDanh sách đơn hàng hiện tại:")
        for index, order in enumerate(order_list, start=1):
            print(f"{index}. {order}")


def statistics_orders():
    pending_count = 0
    delivering_count = 0
    completed_count = 0
    cancelled_count = 0

    for order in order_list:

        if "PENDING" in order:
            pending_count += 1

        elif "DELIVERING" in order:
            delivering_count += 1

        elif "COMPLETED" in order:
            completed_count += 1

        elif "CANCELLED" in order:
            cancelled_count += 1

    print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
    print(f"PENDING: {pending_count}")
    print(f"DELIVERING: {delivering_count}")
    print(f"COMPLETED: {completed_count}")
    print(f"CANCELLED: {cancelled_count}")
    print(f"Tổng số đơn hàng: {len(order_list)}")

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    if not choice.isdigit() or int(choice) not in range(1, 5):
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)

    if choice == 1:
        display_orders()

    elif choice == 2:

        while True:

            print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
            print("1. Thêm đơn hàng mới")
            print("2. Sửa đơn hàng theo vị trí")
            print("3. Xóa đơn hàng theo vị trí")
            print("4. Quay lại menu chính")

            sub_choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

            # ===== Kiểm tra menu con =====
            if not sub_choice.isdigit() or int(sub_choice) not in range(1, 5):
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
                continue

            sub_choice = int(sub_choice)

            if sub_choice == 1:

                order_code = input("Nhập mã đơn hàng: ").strip().upper()
                order_status = input("Nhập trạng thái đơn hàng: ").strip().upper()

                if order_code == "" or order_status == "":
                    print("Không được để trống dữ liệu!")
                    continue

                if order_status not in valid_status:
                    print("Trạng thái đơn hàng không hợp lệ!")
                    continue

                new_order = f"{order_code} - {order_status}"

                order_list.append(new_order)

                print("Thêm đơn hàng thành công!")

            elif sub_choice == 2:

                if not order_list:
                    print("Danh sách đơn hàng hiện đang trống.")
                    continue

                position = input("Nhập vị trí đơn hàng cần sửa: ").strip()

                if not position.isdigit():
                    print("Vị trí không hợp lệ!")
                    continue

                position = int(position)

                # Chuyển sang index Python
                index = position - 1

                if index < 0 or index >= len(order_list):
                    print("Không tồn tại đơn hàng ở vị trí này")
                    continue

   
                new_code = input("Nhập mã đơn hàng mới: ").strip().upper()
                new_status = input("Nhập trạng thái mới: ").strip().upper()

                if new_code == "" or new_status == "":
                    print("Không được để trống dữ liệu!")
                    continue

                if new_status not in valid_status:
                    print("Trạng thái đơn hàng không hợp lệ!")
                    continue

 
                updated_order = f"{new_code} - {new_status}"

                order_list[index] = updated_order

                print("Cập nhật đơn hàng thành công!")

            elif sub_choice == 3:

                if not order_list:
                    print("Danh sách đơn hàng hiện đang trống.")
                    continue

                position = input("Nhập vị trí đơn hàng cần xóa: ").strip()

                # Kiểm tra vị trí hợp lệ
                if not position.isdigit():
                    print("Vị trí không hợp lệ!")
                    continue

                position = int(position)

                # Chuyển sang index Python
                index = position - 1

                if index < 0 or index >= len(order_list):
                    print("Không tồn tại đơn hàng ở vị trí này")
                    continue

                deleted_order = order_list.pop(index)

                print("Đã xóa đơn hàng:", deleted_order)


            elif sub_choice == 4:
                break


    elif choice == 3:
        statistics_orders()


    elif choice == 4:
        print("Thoát chương trình.")
        break