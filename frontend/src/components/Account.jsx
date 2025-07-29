import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import { useState } from 'react';
import { useProvider } from '../providers/Provider';
function NewAccount() {
    const { setDisplayName, email, setEmail, setIsLoggedIn, isLoggedIn } = useProvider();
    const [password, setPassword] = useState("");

    const handleLogin = async () => {
        const response = await fetch("http://localhost:5000/dang-nhap",
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email, password })
            }
        ).then(response => response.json());
        console.log("handleLogin in Account", response)
        setDisplayName(response.user.name)
        setIsLoggedIn(true);
    }

    const handleLogout = async () => {
        const response = await fetch("http://localhost:5000/dang-xuat",
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email, password })
            }
        ).then(response => response.json());
        console.log("handleLogout in Account", response)
        setDisplayName("")
        setEmail("");
        setPassword("");
        setIsLoggedIn(false);
    }
    return (
        <>
            <div
                className="modal fade"
                id="exampleModal"
                tabIndex={-1}
                aria-labelledby="exampleModalLabel"
                aria-hidden="true"
            >
                <div className="modal-dialog">
                    <div className="modal-content">
                        <div className="modal-header">
                            <h1 className="modal-title fs-5" id="exampleModalLabel">
                                Đăng nhập
                            </h1>
                            <button
                                type="button"
                                className="btn-close"
                                data-bs-dismiss="modal"
                                aria-label="Close"
                            />
                        </div>
                        <div className="modal-body">
                            <div className="mb-3">
                                <label htmlFor="exampleFormControlInput1" className="form-label">Email address</label>
                                <input value={email} onChange={(event) => setEmail(event.target.value)} type="email" className="form-control" placeholder="name@example.com"></input>
                            </div>
                            <div className="mb-3">
                                <label htmlFor="exampleFormControlInput1" className="form-label">Mật khẩu</label>
                                <input value={password} onChange={(event) => setPassword(event.target.value)} type="password" className="form-control" placeholder="*"></input>
                            </div>
                            <button onClick={handleLogin} type="submit" className="btn btn-primary me-3">Đăng nhập</button>
                            <button onClick={handleLogout} type="submit" className="btn btn-primary">Đăng xuất</button>
                            {isLoggedIn && (<div className="mt-3 alert alert-success d-flex align-items-center " role="alert">
                                <i className="bi bi-check-circle-fill me-2" style={{ fontSize: "1.5rem" }}></i>
                                <div>
                                    Đăng nhập thành công!
                                </div>
                            </div>)}

                        </div>
                    </div>
                </div>
            </div>

        </>
    )
}

export default NewAccount;
