# Bookstore Management - Backend API Guide for Frontend Developers

## 1. API Base URL

All API endpoints are available at:

```
http://localhost:8000/api/
```

---

## 2. API Endpoints by Page

### **Tất Cả Sách (All Books)**
- **Endpoint:** `/api/sach/`
- **Methods:** `GET`, `POST`, `PUT`, `DELETE`
- **Filters:**  
  - `ten_sach` (book name, partial match)
  - `tac_gia` (author, partial match)
  - `the_loai` (genre, partial match)
  - `nxb` (publisher, partial match)
  - `nam_xb`, `nam_xb_min`, `nam_xb_max` (year, min/max)
  - `slton_min`, `slton_max` (stock, min/max)
- **Example:**  
  `GET /api/sach/?ten_sach=python&slton_min=10`

---

### **Khách Hàng (Customers)**
- **Endpoint:** `/api/khachhang/`
- **Methods:** `GET`, `POST`, `PUT`, `DELETE`
- **Filters:**  
  - `id` (customer ID)
  - `name` (customer name, partial match)
  - `phone` (phone number, partial match)
  - `invoiceId` (invoice ID, partial match)
- **Example:**  
  `GET /api/khachhang/?name=nguyen`

---

### **Nhập Sách (Book Import)**
- **Endpoint:** `/api/phieunhapsach/`
- **Methods:** `GET`, `POST`, `PUT`, `DELETE`
- **Filters:**  
  - `maNhap` (import receipt ID)
  - `ngayNhap` (import date)
  - `maSach` (book ID)
  - `tenSach` (book name, partial match)
- **Example:**  
  `GET /api/phieunhapsach/?ngayNhap=2024-06-01`

---

### **Thanh Toán (Payments/Invoices)**
- **Endpoint:** `/api/hoadon/`
- **Methods:** `GET`, `POST`, `PUT`, `DELETE`
- **Filters:**  
  - `maHD` (invoice ID)
  - `ngayLap` (date)
  - `maKH` (customer ID)
  - `tenKH` (customer name, partial match)
- **Example:**  
  `GET /api/hoadon/?maKH=1`

---

### **Phiếu Thu Tiền (Receipts)**
- **Endpoint:** `/api/phieuthutien/`
- **Methods:** `GET`, `POST`, `PUT`, `DELETE`
- **Filters:** (not yet implemented, but you can request by ID or customer)

---

### **Báo Cáo Tồn (Inventory Report)**
- **Endpoint:** `/api/baocaoton/`
- **Methods:** `GET`, `POST`, `PUT`, `DELETE`
- **Filters:**  
  - `thang` (month)
  - `nam` (year)
  - `maSach` (book ID)
  - `tenSach` (book name, partial match)
  - `tonDau`, `tonCuoi` (stock at start/end)
- **Example:**  
  `GET /api/baocaoton/?thang=6&nam=2024`

---

### **Báo Cáo Công Nợ (Debt Report)**
- **Endpoint:** `/api/baocaocongno/`
- **Methods:** `GET`, `POST`, `PUT`, `DELETE`
- **Filters:**  
  - `thang`, `nam`
  - `maKH` (customer ID)
  - `tenKH` (customer name, partial match)
  - `noDau`, `noCuoi` (debt at start/end)
- **Example:**  
  `GET /api/baocaocongno/?maKH=1`

---
## 3. Authentication

Most API endpoints require you to be logged in and have the correct permissions.

### Available superuser account:
- username: minfu_2k5
- password: bum#25102005

### How to get an account

You can ask the backend team to create an account for you, or (if you have permission) use the API:

**Example: Create a user account (POST `/api/usermanagement/`)**

```json
POST http://localhost:8000/api/usermanagement/
Content-Type: application/json

{
  "username": "frontend_user",
  "password": "yourpassword",
  "email": "frontend@example.com",
  "first_name": "Frontend",
  "last_name": "User",
  "role": "NguoiNhap"   // or "ThuNgan"
}
```
- The `role` field assigns the user to a group (must be one of the allowed group names).

---

### How to create group model permissions

**Example: Create a group model permission (POST `/api/groupmodelpermission/`)**

```json
POST http://localhost:8000/api/groupmodelpermission/
Content-Type: application/json

{
  "group": 2,                // group ID (ask backend or check /api/groups/)
  "model_name": "Sach",      // model name, e.g. "Sach", "KhachHang"
  "can_view": true,
  "can_add": false,
  "can_change": false,
  "can_delete": false
}
```
- Only admins/managers can do this.  
- You can view all group permissions at `/api/groupmodelpermission/`.

---

### How to log in and use your token

**Example: Log in and get a JWT token (POST `/api/token/`)**

```json
POST http://localhost:8000/api/token/
Content-Type: application/json

{
  "username": "frontend_user",
  "password": "yourpassword"
}
```
- The response will include an `access` token.  
- For all subsequent API requests, add this header:
  ```
  Authorization: Bearer <your_token>
  ```

**If you get a 403 or 401 error, you may not be logged in or lack permission for that action.**


---

## 4. How to Use the API in Your Frontend

**Step-by-step:**

1. **Import axios or use fetch** in your React component.
2. **Call the API endpoint** for the data you need.  
   Example using axios:
   ```js
   import axios from 'axios';

   // Example: Get all books with filter
   axios.get('http://localhost:8000/api/sach/', {
     params: { ten_sach: 'python' },
     headers: { Authorization: `Bearer ${yourToken}` }
   })
   .then(res => setBooks(res.data))
   .catch(err => console.error(err));
   ```

3. **Use query parameters** for filtering (see the endpoint/filter tables above).
   - Example: `/api/khachhang/?name=nguyen`
   - Example: `/api/hoadon/?maKH=1&ngayLap=2024-06-01`

4. **POST/PUT/DELETE**:  
   - For creating or updating, send JSON data in the request body.
   - Example:
     ```js
     axios.post('http://localhost:8000/api/khachhang/', {
       HoTen: 'Nguyen Van A',
       DienThoai: '0123456789',
       // ...other fields
     }, {
       headers: { Authorization: `Bearer ${yourToken}` }
     })
     ```

5. **Check the response**:  
   - Data will be returned as JSON.
   - If you get errors, check the error message for missing fields or permissions.

### Basic usage with axios/fetch

**Example: Get all books with a filter**
```js
import axios from 'axios';

axios.get('http://localhost:8000/api/sach/', {
  params: { ten_sach: 'python' },
  headers: { Authorization: `Bearer ${yourToken}` }
})
.then(res => setBooks(res.data))
.catch(err => console.error(err));
```

**Example: Create a new customer**
```js
axios.post('http://localhost:8000/api/khachhang/', {
  HoTen: 'Nguyen Van A',
  DienThoai: '0123456789',
  // ...other fields
}, {
  headers: { Authorization: `Bearer ${yourToken}` }
})
```

**Example: Filter invoices by customer and date**
```
GET http://localhost:8000/api/hoadon/?maKH=1&ngayLap=2024-06-01
```
---

## 5. Need Help?

- **If you need a new API or filter:**  
  Tell the backend team what data you need and how you want to filter it. We can quickly add new endpoints or filters.

- **If you get errors:**  
  - Double-check your endpoint URL and parameters.
  - Make sure you are authenticated (see section 3).
  - Read the error message in the response for hints.

- **If you’re unsure about request/response format:**  
  - Ask the backend team for a sample.
  - Or, use Postman to try the endpoint and see the JSON structure.

- **For more details:**  
  - See the backend code in `api/views.py` and `api/serializers.py`.
  - Or just ask us directly!

---

