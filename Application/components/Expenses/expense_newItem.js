import { createRef, useState, useEffect } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChevronUp, faChevronDown, faMinus} from "@fortawesome/free-solid-svg-icons";
import constant from "../../constants";
import API_CALLS from "../../app/api/api_routes";


export default function ExpenseNewItem({ category, submit_item }) {

    const [newtype, setNewType] = useState(false);
    const expense_category = createRef(), expense_amount = createRef(), expense_note = createRef(), expense_date = createRef();

    const [item, setItem] = useState({ 
        id: 0,
        expense_paid_by: "default",
        expense_category: undefined,
        expense_note: undefined,
        expense_amount: undefined,
        expense_avatar: "default.png",
        expense_type: newtype ? "Expense" : "Income",
        expense_date: constant.getCurrentDate(),
        expense_key: undefined,
    });

    useEffect(() => {
        const item_new_key = () => setItem(prevState => ({ ...prevState, expense_key: constant.UUID4().split("-").pop() }))
        item_new_key();
    }, []);

    const change_expense_type = (value) => {
        setNewType(value);
        setItem((prevState) => ({...prevState, expense_type: value ? "Expense" : "Income"}))
    }
    

    return (
        <div className="expenses_newItem">
            <div className="expense_type">
                <div className={"selected_type " + (newtype ? "right" : "left")}></div>
                <span onClick={() => change_expense_type(false)}>Expense</span>
                <span onClick={() => change_expense_type(true)}>Income</span>
            </div>
            <div className="exp expense_category_service">
                <label htmlFor="expense_categoryInput" style={{ marginBottom: 5 }}>Expense Category</label>
                <input name="expense_category" type="text" id="expense_categoryInput" placeholder="Enter Category Name" 
                    ref={expense_category} value={item?.expense_category || ""}
                    onChange={(e) => setItem((prevState) => ({ ...prevState, expense_category: e.target.value }))}
                    // onKeyDown={(e) => _pick_item(e)}
                />
            </div>
            <div className="exp expense_amount_service">
                <label htmlFor="expense_amountInput" style={{ marginBottom: 5 }}>Expense Amount</label>
                <input name="expense_amount" type="text" id="expense_amountInput" placeholder="Enter Amount" 
                    ref={expense_amount} value={item?.expense_amount || ""}
                    onChange={(e) => setItem((prevState) => ({ ...prevState, expense_amount: e.target.value }))}
                    // onKeyDown={(e) => _pick_item(e)}
                />
            </div>
            <div className="account expense_paid_by_service">
                <div className="account_title">
                    <label htmlFor="barcodeInput" style={{  }}>Pick Account/Card</label>
                </div>
                <div className="selected">
                    <input type="text" disabled={true} defaultValue={item?.expense_paid_by || ""}/>
                    <div className='chevrons' onClick={() => console.log("Picking Card!")}>
                        <FontAwesomeIcon icon={faChevronUp} style={{ fontSize: 10, color: "#fff" }} />
                        <FontAwesomeIcon icon={faChevronDown} style={{ fontSize: 10, color: "#fff" }} />
                    </div> 
                </div>
            </div>
            <div className="exp expense_note_service">
                <label htmlFor="expense_noteInput" style={{ marginBottom: 5 }}>Expense Note</label>
                <textarea name="expense_note" type="text" id="expense_noteInput" placeholder="Type a note ..." 
                    ref={expense_note} value={item?.expense_note || ""}
                    onChange={(e) => setItem((prevState) => ({ ...prevState, expense_note: e.target.value }))}
                    // onKeyDown={(e) => _pick_item(e)}
                >
                </textarea>
            </div>
            <div className="exp expense_date_service">
                <label htmlFor="expense_dateInput" style={{ marginBottom: 5 }}>Expense Date</label>
                <input name="expense_date" type="text" id="expense_dateInput" placeholder="Enter Date" 
                    ref={expense_date} value={item?.expense_date || ""}
                    onChange={(e) => setItem((prevState) => ({ ...prevState, expense_date: e.target.value }))}
                    // onKeyDown={(e) => _pick_item(e)}
                />
            </div>
            <div className="button">
                <button>
                    <FontAwesomeIcon icon={faMinus} style={{ fontSize: 24, color: "#fff" }} />
                </button>
                <button onClick={() => submit_item("expense", item)}>Append Transaction</button>
            </div>
        </div>
    )
}