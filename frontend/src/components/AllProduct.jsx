import { useState, useEffect } from 'react'
import ProductCard from "./ProductCard"
import { useProvider } from '../providers/Provider';


const normalize = (str) =>
  str
    .normalize("NFD")                         // remove diacritics
    .replace(/[\u0300-\u036f]/g, "")         // remove combining marks
    .replace(/\s+/g, " ")                    // collapse multiple spaces into one
    .trim()                                  // remove leading/trailing spaces
    .toLowerCase();                          // make case-insensitive


function AllProduct() {
  const { allProductSearchInput, setAllProductSearchInput } = useProvider();
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
      <div className="input-group search-bar">
        <div className="form-outline" data-mdb-input-init="">
          <input value={allProductSearchInput} onChange={(event) => setAllProductSearchInput(event.target.value)} type="search" id="form1" className="form-control" placeholder="Tìm sản phẩm" />
        </div>
      </div>


      <div className="container mt-5">
        {loading && <p>Đang tải sản phẩm...</p>}
        {error && <p className="text-danger">Lỗi: {error}</p>}

        <div className="row">
          {allProductSearchInput.length === 0 ?
            products.map(product => (
              <div className="col-sm-3 mb-4" key={product.id}>
                <ProductCard product={product} />
              </div>
            )) :
            products
              .filter(product =>
                normalize(product.name).includes(normalize(allProductSearchInput))
              )
              .map(product => (
                <div className="col-sm-3 mb-4" key={product.id}>
                  <ProductCard product={product} />
                </div>
              ))
          }
        </div>
      </div>
    </>
  )
}

export default AllProduct;