import { createRef, useState } from "react"




export default function ProductSettings({}) {

    const discount_percentage = createRef(), profit_percentage = createRef();
    const [productItem, setProductItem] = useState({
        discount_percentage: 5,
        profit_percentage: 35,
        off_stock_min: 3,
    });

    return (
        <div>
            <div className="product_detail_settings">
                <div className="product_detail_title">Products Settings</div>
                <div className="product_detail_inputs">
                    <div className="set discount_percentage">
                        <label htmlFor="discount_percentageInput" className={productItem?.discount_percentage ? "show" : ""}>Discount Percentage (%)</label>
                        <input name="discount_percentage" type="text" id="discount_percentageInput" placeholder="Discount Percentage" 
                            ref={discount_percentage} value={productItem?.discount_percentage || ""}
                            // onChange={(e) => setProductItem((prevState) => ({ ...prevState, discount_percentage: e.target.value }))}
                        />
                    </div>
                    <div className="set profit_percentage">
                        <label htmlFor="profit_percentageInput" className={productItem?.profit_percentage ? "show" : ""}>Profit Percentage (%)</label>
                        <input name="profit_percentage" type="text" id="profit_percentageInput" placeholder="Profit Percentage" 
                            ref={profit_percentage} value={productItem?.profit_percentage || ""}
                            // onChange={(e) => setProductItem((prevState) => ({ ...prevState, profit_percentage: e.target.value }))}
                        />
                    </div>
                    <div className="set off_stock_min">
                        <label htmlFor="off_stock_minInput" className={productItem?.off_stock_min ? "show" : ""}>Off Stock Minimum (Unit)</label>
                        <input name="off_stock_min" type="text" id="off_stock_minInput" placeholder="Off Stock Minimum" 
                            ref={profit_percentage} value={productItem?.off_stock_min || ""}
                            // onChange={(e) => setProductItem((prevState) => ({ ...prevState, profit_percentage: e.target.value }))}
                        />
                    </div>
                </div>
            </div>
        </div>
    )
}