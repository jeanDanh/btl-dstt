import { useState, useEffect } from 'react'
import ProductCard from "./ProductCard"

function AllProduct() {
  const [products, setProducts] = useState([]) 
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch("http://localhost:5000/danh-sach-san-pham")
      .then(res => {
        if (!res.ok) throw new Error("Network response was not ok")
        return res.json()
      })
      .then(data => {
        setProducts(data)
        setLoading(false)
      })
      .catch(err => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  return (
    <>
      <div className="container mt-5">
        {loading && <p>Đang tải sản phẩm...</p>}
        {error && <p className="text-danger">Lỗi: {error}</p>}

        <div className="row">
          {products.map(product => (
            <div className="col-sm-3 mb-4" key={product.id}>
              <ProductCard product={product} />
            </div>
          ))}
        </div>
      </div>
    </>
  )
}

export default AllProduct;