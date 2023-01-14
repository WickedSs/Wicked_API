


import { useState, useEffect } from "react";
import API_CALLS from "../../pages/api/api_routes";
import ProductItem from "./product_item";


export default function ProductOutOfTable({}) {

    const [currentProducts, setCurrentProducts] = useState([]);
    useEffect(() => {
        const fetch_products = async () => {
            const response = await API_CALLS.SELECT("product", "quantity", 5, 3103);
            console.log(response);
            if (response?.status !== undefined) {
                setCurrentProducts(response.data);
            }
        }
        fetch_products();
    }, []);

    return (
        <div className="table">
            <div className="products_table">
                { currentProducts.map((item, index) => <ProductItem _item={item} />) }
                { currentProducts.map((item, index) => <ProductItem _item={item} />) }
                { currentProducts.map((item, index) => <ProductItem _item={item} />) }
            </div>
        </div>
    )
}