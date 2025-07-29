import { BrowserRouter as Router, Routes, Route, NavLink } from "react-router-dom";
import AllProduct from "./components/AllProduct";
import ProductPurchased from "./components/ProductPurchased";
import ProductPropose from "./components/ProductPropose";
import Account from './components/Account';
import "./App.css";

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

import { useAuth } from '../src/providers/Auth';


function App() {
  const { displayName, email, isLoggedIn } = useAuth();


  return (
    <Router>
      <div className="container-fluid text-white head-bar">
        <img src="https://mybk.hcmut.edu.vn/my/images/logo.png" alt="Logo" className="logo" />
        {isLoggedIn === false ?
          (
            <button type="button" className="btn btn-light account-nav" data-bs-toggle="modal" data-bs-target="#exampleModal">
              Tài khoản
            </button>
          ) :
          (
            <div className="hover-turn-yellow card account-nav" data-bs-toggle="modal" data-bs-target="#exampleModal" style={{ width: "18rem" }}>
              <div className="card-body">
                <h5 className="card-title">{displayName}</h5>
                <p className="card-text">
                  {email}
                </p>
              </div>
            </div>)
        }
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
        </ul>
        <Account />
      </div>

      <div className="container mt-4">
        <Routes>
          <Route path="/" element={<AllProduct />} />
          <Route path="/da-mua" element={<ProductPurchased />} />
          <Route path="/de-xuat" element={<ProductPropose />} />
        </Routes>
      </div>

    </Router>
  );
}

export default App;
