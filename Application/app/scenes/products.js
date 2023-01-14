import { useState, createRef } from "react"
import ProductTable from "../../components/Products/products_table";

import '../../styles/products.css';





export default function Products() {

    const modeRef = createRef();
    const [mode, setMode] = useState(0);
    const border_colors = [["#3a86ff", "#ffffff"], ["#38a3a5", "#ffffff"], ["#bc4749", "#ffffff"]];

    const _changeMode = (mode, active) => {
        setMode(mode);
        modeRef.current.className = "selected_mode " + active;
    }

    return (
        <div className="master_scene">
            <div className="top_area">
                <div className="search_bar">
                    <input type="text" placeholder={(mode === 1 ? "Disabled" : "Search by name, barcode or category")} disabled={mode === 1 ? true : false} />
                </div>
                <div className="modes">
                    <div className="selected_mode inspect" ref={modeRef} style={{ backgroundColor: border_colors[mode][0] }}></div>
                    <div className={"action_button inspect" + ( mode == 0 ? " mode_active" : "" )} onClick={() => _changeMode(0, "inspect")}>Inspect</div>
                    <div className={"action_button new" + ( mode == 1 ? " mode_active" : "" )} onClick={() => _changeMode(1, "new")}>New</div>
                    <div className={"action_button stock" + ( mode == 2 ? " mode_active" : "" )} onClick={() => _changeMode(2, "stock")} >Out Of Stock!</div>
                </div>
            </div>
            <ProductTable _mode={mode} />
        </div>
    )
}