import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import { useState, useEffect } from 'react';

const TestLogin = () => {
    const [data, setData] = useState(null);
    useEffect(() => {
        const getData = async () => {
            const response = await fetch("http://localhost:5000/nguoi-dung").then(response => response.json());
            setData(response);
            console.log("Fetched data", response);
        }
        getData();
    }, [])

    return (
        <div>
            <h2>User info </h2>
            {
                !data ? (
                    <p>Loading...</p>
                ) : data.status === true ? (
                    <div>
                        <p><strong>Name:</strong> {data.user.name}</p>
                        <p><strong>Email:</strong> {data.user.email}</p>
                        <p><strong>ID:</strong> {data.user.id}</p>
                    </div>
                ) : (
                    <p style={{ color: "red" }}>{data.message}</p>
                )
            }
        </div>
    );
}

function Account() {
    return (
        <>
            <div className="mb-3">
                <label htmlFor="exampleFormControlInput1" className="form-label">Email address</label>
                <input type="email" className="form-control" id="exampleFormControlInput1" placeholder="name@example.com"></input>
            </div>
            <div className="mb-3">
                <label htmlFor="exampleFormControlInput1" className="form-label">Mật khẩu</label>
                <input type="password" className="form-control" id="exampleFormControlInput1" placeholder="*"></input>
            </div>
            <button type="submit" className="btn btn-primary me-3">Đăng nhập</button>
            <button type="submit" className="btn btn-primary">Đăng xuất</button>
            <TestLogin />
        </>
    )
}
// Ý tưởng về luồng hoạt động: khi tôi nhấn nút Đăng nhập, nút sẽ gọi hàm TestLogin, tất cả những gì điền trong form sẽ được truyền vào
export default Account;