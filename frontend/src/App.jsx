import { BrowserRouter as Router, Routes, Route, NavLink } from "react-router-dom";
import AllProduct from "./components/AllProduct";
import ProductPurchased from "./components/ProductPurchased";
import ProductPropose from "./components/ProductPropose";
import Account from './components/Account';
import NewAccount from './components/NewAccount';
import "./App.css";

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

function App() {
  return (
    <Router>
      <div className="container-fluid text-white head-bar">
        <img src="https://mybk.hcmut.edu.vn/my/images/logo.png" alt="Logo" className="logo" />
        <button type="button" className="btn btn-light account-nav" data-bs-toggle="modal" data-bs-target="#exampleModal">
          Tài khoản
        </button>
      </div>


      <div className="container-fluid text-white tool-bar">
        <ul className="nav">
          <li className="nav-item">
            <NavLink to="/" end className="nav-link custom-nav">Sản phẩm</NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/da-mua" className="nav-link custom-nav">Đã mua</NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/de-xuat" className="nav-link custom-nav">Đề xuất</NavLink>
          </li>
          {/* <li className="nav-item">
            <NavLink to="/tai-khoan" className="nav-link custom-nav">Tài khoản (cũ)</NavLink>
          </li> */}
        </ul>
        <NewAccount />
      </div>

      <div className="container mt-4">
        <Routes>
          <Route path="/" element={<AllProduct />} />
          <Route path="/da-mua" element={<ProductPurchased />} />
          <Route path="/de-xuat" element={<ProductPropose />} />
          {/* <Route path="/tai-khoan" element={<Account />} /> */}
        </Routes>
      </div>

    </Router>
  );
}

export default App;
