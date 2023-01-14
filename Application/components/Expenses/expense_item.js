
import { useState } from "react"
import constant from "../../constants"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash } from "@fortawesome/free-solid-svg-icons";

export default function ExpenseItem({ item }) {

    const [isHover, setHover] = useState(true);
    const type = item?.expense_type == "Expense" ? false : true || "";

    return (
        <div className="expense_item">
            <div className="expense_item_details">
                <div style={{ fontSize: "1.2em" }}>{item?.expense_category || "Service Name"}</div>
                <div>{item?.expense_note || "Dinner with friend."}</div>
            </div>
            <div className="expense_item_price_date">
                <div style={{ color: type ? "#38a3a5" : "#bc4749", fontSize: "1.2em" }}>{type ? "+" : "-"}{constant.formatter(item?.expense_amount || 1500)}</div>
                <div>{item?.expense_date || constant.getCurrentDate()}</div>
            </div>
            <div className="expense_item_delete">
                <FontAwesomeIcon icon={faTrash} style={{ fontSize: 20, color: "#fff" }} />
            </div>
        </div>
    )
}