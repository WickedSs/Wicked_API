import Image from "next/image"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlus } from "@fortawesome/free-solid-svg-icons";

import default_png from '../../images/default.png'
import default_2_png from '../../images/default_2.jpg'
import { createRef, useEffect, useState } from "react";
import constant from "../../constants";

export default function ProductNewItem({ _show }) {

    const hiddenFileInput = createRef();
    const [newItems, setNewItems] = useState([]);
    const [workingItem, setWorkingItem] = useState({});

    useEffect(() => {
        setWorkingItem(newItems.length > 0 ? newItems[newItems.length - 1] : {});
        console.log(newItems);
    }, [newItems]);

    const _hiddenFileInput = () => hiddenFileInput.current.click();
    const _update_item = (index) => {

    }
    const _handleChange = (e) => {
        if (e.target.files && e.target.files[0]) {
            const file = e.target.files[0];
            let new_product = constant.product_base;
            new_product.preview = file;
            setNewItems((prevState) => [...prevState, new_product]);
        }
    }


    return (
        <div className="product_new_item" style={{ height: _show == 1 ? "12.5em" : "0em" }}>
            <div className="product_information">
                <div className="products_previews">
                    <div className="new_product_add" onClick={() => _hiddenFileInput()}>
                        <FontAwesomeIcon icon={faPlus} style={{ fontSize: 64, color: "#888" }} />
                        <input type="file" ref={hiddenFileInput} onChange={_handleChange} accept="image/*" style={{ display: 'none' }} />
                    </div>
                    { newItems.map((item, index) => (
                        <div className="avatar_in_progress">
                            <Image src={default_png} objectFit="cover" />
                        </div>
                    ))}
                </div>
                <div className="product_data">
                    <div className="inline name_category_bought">
                        <div className="vbox_new product_link">
                            <label htmlFor="barcodeInput" style={{ marginBottom: 5 }}>Link</label>
                            <input name="barcode" type="text" id="barcodeInput" disabled={true} 
                                // value={constant.UUID4().split("-").pop()}
                                onChange={(e) => setItem((prevState) => ({
                                    ...prevState, barcode: e.target.value
                                }))}
                                onKeyDown={(e) => _pick_item(e)}
                            />
                        </div>
                        <div className="vbox_new product_name">
                            <label htmlFor="barcodeInput" style={{ marginBottom: 5 }}>Name</label>
                            <input name="barcode" type="text" id="barcodeInput" placeholder="Enter Name" 
                                // ref={barcodeRef} value={item.barcode || ""}
                                onChange={(e) => setItem((prevState) => ({
                                    ...prevState, barcode: e.target.value
                                }))}
                                onKeyDown={(e) => _pick_item(e)}
                            />
                        </div>
                        <div className="vbox_new product_category">
                            <label htmlFor="barcodeInput" style={{ marginBottom: 5 }}>Category</label>
                            <input name="barcode" type="text" id="barcodeInput" placeholder="Enter Category" 
                                // ref={barcodeRef} value={item.barcode || ""}
                                onChange={(e) => setItem((prevState) => ({
                                    ...prevState, barcode: e.target.value
                                }))}
                                onKeyDown={(e) => _pick_item(e)}
                            />
                        </div>
                        <div className="vbox_new product_bought">
                            <label htmlFor="barcodeInput" style={{ marginBottom: 5 }}>Bought</label>
                            <input name="barcode" type="text" id="barcodeInput" placeholder="Enter Price" 
                                // ref={barcodeRef} value={item.barcode || ""}
                                onChange={(e) => setItem((prevState) => ({
                                    ...prevState, barcode: e.target.value
                                }))}
                                onKeyDown={(e) => _pick_item(e)}
                            />
                        </div>
                        <div className="vbox_new product_color">
                            <label htmlFor="barcodeInput" style={{ marginBottom: 5 }}>Color</label>
                            <input name="barcode" type="text" id="barcodeInput" placeholder="Enter Color" 
                                // ref={barcodeRef} value={item.barcode || ""}
                                onChange={(e) => setItem((prevState) => ({
                                    ...prevState, barcode: e.target.value
                                }))}
                                onKeyDown={(e) => _pick_item(e)}
                            />
                        </div>
                    </div>
                    <div className="inline barcode_quantity_price">
                        <div className="vbox_new product_name">
                            <label htmlFor="barcodeInput" style={{ marginBottom: 5 }}>Barcode</label>
                            <input name="barcode" type="text" id="barcodeInput" placeholder="Enter Barcode" 
                                // ref={barcodeRef} value={item.barcode || ""}
                                onChange={(e) => setItem((prevState) => ({
                                    ...prevState, barcode: e.target.value
                                }))}
                                onKeyDown={(e) => _pick_item(e)}
                            />
                        </div>
                        <div className="vbox_new product_category">
                            <label htmlFor="barcodeInput" style={{ marginBottom: 5 }}>Quantity</label>
                            <input name="barcode" type="text" id="barcodeInput" placeholder="Enter Qte" 
                                // ref={barcodeRef} value={item.barcode || ""}
                                onChange={(e) => setItem((prevState) => ({
                                    ...prevState, barcode: e.target.value
                                }))}
                                onKeyDown={(e) => _pick_item(e)}
                            />
                        </div>
                        <div className="vbox_new product_bought">
                            <label htmlFor="barcodeInput" style={{ marginBottom: 5 }}>Price</label>
                            <input name="barcode" type="text" id="barcodeInput" disabled={true}
                                // ref={barcodeRef} value={item.barcode || ""}
                                onChange={(e) => setItem((prevState) => ({
                                    ...prevState, barcode: e.target.value
                                }))}
                                onKeyDown={(e) => _pick_item(e)}
                            />
                        </div>
                        <div className="vbox_new product_bought">
                            <label htmlFor="barcodeInput" style={{ marginBottom: 5 }}>Market</label>
                            <input name="barcode" type="text" id="barcodeInput"
                                // ref={barcodeRef} value={item.barcode || ""}
                                onChange={(e) => setItem((prevState) => ({
                                    ...prevState, barcode: e.target.value
                                }))}
                                onKeyDown={(e) => _pick_item(e)}
                            />
                        </div>
                        <div className="button">
                            <button>CLEAR</button>
                        </div>
                        <div className="button">
                            <button>APPEND</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}