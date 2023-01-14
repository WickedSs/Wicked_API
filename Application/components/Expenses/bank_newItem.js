import { useEffect, useState, createRef } from "react"
import constant from "../../constants";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlus, faMinus, faCheck } from "@fortawesome/free-solid-svg-icons";


export default function NewBank({ newState, submit_item }) {

    const {state, setState} = newState;
    const bank_name = createRef(), bank_holder_name = createRef(), bank_bank_number = createRef(), bank_card_number = createRef();
    const bank_card_expiration = createRef(), bank_card_type = createRef(), bank_amount = createRef();
    
    const [cardState, setCardState] = useState(false);
    const [item, setItem] = useState({
        id: 0,
        bank_name: undefined,
        bank_holder_name: undefined,
        bank_amount: undefined,
        bank_bank_number: undefined,
        bank_card_number: undefined,
        bank_card_expiration: undefined,
        bank_card_type: undefined,
        bank_key: undefined
    });

    useEffect(() => {
        const item_new_key = () => setItem(prevState => ({ ...prevState, bank_key: constant.UUID4().split("-").pop() }))
        item_new_key();
    }, []);

    return (
        <div className={"new_bank " + (state ? "" : "hide")}>
            <div className="exp bank_name">
                <label htmlFor="bank_nameInput" className={item?.bank_name ? "show" : ""}>Bank Name</label>
                <input name="bank_name" type="text" id="bank_nameInput" placeholder="Bank Name" 
                    ref={bank_name} value={item?.bank_name || ""}
                    onChange={(e) => setItem((prevState) => ({ ...prevState, bank_name: e.target.value }))}
                />
            </div>
            <div className="exp bank_holder_name">
                <label htmlFor="bank_holder_nameInput" className={item.bank_holder_name ? "show" : ""}>Bank Holder Name</label>
                <input name="bank_holder_name" type="text" id="bank_holder_nameInput" placeholder="Bank Holder Name" 
                    ref={bank_holder_name} value={item?.bank_holder_name || ""}
                    onChange={(e) => setItem((prevState) => ({ ...prevState, bank_holder_name: e.target.value }))}
                />
            </div>
            <div className="exp bank_bank_number">
                <label htmlFor="bank_bank_numberInput" className={item.bank_bank_number ? "show" : ""}>Bank Number</label>
                <input name="bank_bank_number" type="text" id="bank_bank_numberInput" placeholder="Bank Account Number" 
                    ref={bank_bank_number} value={item?.bank_bank_number || ""}
                    onChange={(e) => setItem((prevState) => ({ ...prevState, bank_bank_number: e.target.value }))}
                />
            </div>
            <div className="exp bank_amount">
                <label htmlFor="bank_amountInput" className={item.bank_amount ? "show" : ""}>Current Balance</label>
                <input name="bank_amount" type="text" id="bank_amountInput" placeholder="Bank Account Balance" 
                    ref={bank_amount} value={item?.bank_amount || ""}
                    onChange={(e) => setItem((prevState) => ({ ...prevState, bank_amount: e.target.value }))}
                />
            </div>
            <div className="exp bank_card_number">
                <label htmlFor="bank_card_numberInput" className={item.bank_card_number ? "show" : ""}>Bank Card Number</label>
                <input name="bank_card_number" type="text" id="bank_card_numberInput" placeholder="Bank Card Number"
                    ref={bank_card_number} value={item?.bank_card_number || ""}
                    onChange={(e) => setItem((prevState) => ({ ...prevState, bank_card_number: e.target.value }))}
                />
            </div>
            <div className="card_details">
                <div className="exp bank_card_expiration">
                    <label htmlFor="bank_card_expirationInput" className={item.bank_card_expiration ? "show" : ""}>Exp Date</label>
                    <input name="bank_card_expiration" type="text" id="bank_card_expirationInput" placeholder="MM/YY"
                        ref={bank_card_expiration} value={item?.bank_card_expiration || ""}
                        onChange={(e) => setItem((prevState) => ({ ...prevState, bank_card_expiration: e.target.value }))}
                    />
                </div>
                <div className="exp bank_card_type">
                    <label htmlFor="bank_card_typeInput" className={item.bank_card_type ? "show" : ""}>Card Type</label>
                    <input name="bank_card_type" type="text" id="bank_card_typeInput" placeholder="Card Type"
                        ref={bank_card_type} value={item?.bank_card_type || ""}
                        onChange={(e) => setItem((prevState) => ({ ...prevState, bank_card_type: e.target.value }))}
                    />
                </div>
            </div>
            <div className="button">
                <button>
                    <FontAwesomeIcon icon={faMinus} style={{ fontSize: 24, color: "#fff" }} />
                </button>
                <button onClick={() => submit_item("bank", item)} >Append Bank</button>
            </div>
        </div>
    )
}