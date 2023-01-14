import { useState, useEffect } from "react";
import API_CALLS from "../../app/api/api_routes";
import ProductItem from "./product_item";
import ProductNewItem from "./product_newItem";


export default function ProductTable({ _mode }) {

    const [currentProducts, setCurrentProducts] = useState([]);
    useEffect(() => {
        const fetch_products = async () => {
            const response = await API_CALLS.SELECT("product", undefined, undefined, 3103);
            if (response?.status !== undefined) {
                setCurrentProducts(response.data);
            }
        }
        fetch_products();
    }, []);

    return (
        <div className="table">
            <ProductNewItem _show={_mode}/>
            <div className="products_table">
                <div className="divide_title" style={{ marginTop: _mode == 1 ? "1em" : "0"}} >
                    List of Products
                </div>
                { currentProducts.map((item, index) => <ProductItem _item={item} />) }
                { currentProducts.map((item, index) => <ProductItem _item={item} />) }
                { currentProducts.map((item, index) => <ProductItem _item={item} />) }
            </div>
        </div>
    )
}