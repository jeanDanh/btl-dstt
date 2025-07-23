import React, { useState } from "react";
import "./ProductCard.css";

function ProductCard({ product }) {
  const [quantity, setQuantity] = useState(1);

  const increaseQuantity = () => {
    setQuantity(quantity + 1);
  };

  const decreaseQuantity = () => {
    if (quantity > 1) {
      setQuantity(quantity - 1);
    }
  };

  return (
    <div className="card h-100 d-flex flex-column">
      <img
        src={product.img}
        className="card-img-top product-image"
        alt={product.name}
      />

      <div className="card-body d-flex flex-column">
        <h6 className="card-title">{product.name}</h6>
        <p className="card-text truncate">{product.describes}</p>

        <div className="mt-auto">
          <p className="card-text fw-bold text-danger fs-5">
            {product.price.toLocaleString()}₫
          </p>

          <div className="d-flex align-items-center mt-2">
            <button className="btn btn-sm flex-grow-1 buy-btn">Mua hàng</button>

            <div className="quantity-control ms-2">
              <button
                className="btn btn-sm quantity-btn"
                onClick={decreaseQuantity}
              >
                −
              </button>
              <input
                type="text"
                value={quantity}
                readOnly
                className="quantity-input"
              />
              <button
                className="btn btn-sm quantity-btn"
                onClick={increaseQuantity}
              >
                +
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ProductCard;
