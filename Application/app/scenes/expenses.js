import { createRef, useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlus, faMinus, faCheck } from "@fortawesome/free-solid-svg-icons";

import '../../styles/expenses.css';
import constant from "../../constants";
import API_CALLS from "../api/api_routes";
import CreditCard from "../../components/Expenses/bank";
import NewBank from "../../components/Expenses/bank_newItem";
import ExpenseItem from "../../components/Expenses/expense_item";
import ExpenseNewItem from "../../components/Expenses/expense_newItem";

function Stat({ _stat }) {
    return (
        <div className="periodic_stat">
            <div>{_stat?.title || "Periodic Amount"}</div>
            <div>{_stat?.sign + "" + constant.formatter(_stat?.amount || 0)}</div>
        </div>
    )
}


export default function Expenses() {

    const [expenses, setExpenses] = useState([]);
    const [banks, setBanks] = useState([
        // { bank_amount: 25000, bank_bank_number: "0799992459687621", bank_card_expiration: "03/24", bank_card_number: "6280703029345631", bank_card_type: "El Dahabia", bank_holder_name: "Souelymane Guerida", bank_key: "d988aec0fc2b", bank_name: "Algerie Poste" },
        // { bank_amount: 25000, bank_bank_number: "0799992459687621", bank_card_expiration: "03/24", bank_card_number: "6280703029345631", bank_card_type: "El Dahabia", bank_holder_name: "Souelymane Guerida", bank_key: "d988aec0fc2b", bank_name: "Algerie Poste" },
        // { bank_amount: 25000, bank_bank_number: "0799992459687621", bank_card_expiration: "03/24", bank_card_number: "6280703029345631", bank_card_type: "El Dahabia", bank_holder_name: "Souelymane Guerida", bank_key: "d988aec0fc2b", bank_name: "Algerie Poste" },
        // { bank_amount: 25000, bank_bank_number: "0799992459687621", bank_card_expiration: "03/24", bank_card_number: "6280703029345631", bank_card_type: "El Dahabia", bank_holder_name: "Souelymane Guerida", bank_key: "d988aec0fc2b", bank_name: "Algerie Poste" },
        // { bank_amount: 25000, bank_bank_number: "0799992459687621", bank_card_expiration: "03/24", bank_card_number: "6280703029345631", bank_card_type: "El Dahabia", bank_holder_name: "Souelymane Guerida", bank_key: "d988aec0fc2b", bank_name: "Algerie Poste" },
        // { bank_amount: 25000, bank_bank_number: "0799992459687621", bank_card_expiration: "03/24", bank_card_number: "6280703029345631", bank_card_type: "El Dahabia", bank_holder_name: "Souelymane Guerida", bank_key: "d988aec0fc2b", bank_name: "Algerie Poste" },
        // { bank_amount: 25000, bank_bank_number: "0799992459687621", bank_card_expiration: "03/24", bank_card_number: "6280703029345631", bank_card_type: "El Dahabia", bank_holder_name: "Souelymane Guerida", bank_key: "d988aec0fc2b", bank_name: "Algerie Poste" },
    ]);
    const [category, setCategories] = useState([]);
    const [state, setState] = useState(false);
    const [total, setTotal] = useState(0);
    const [hasMounted, setHasMounted] = useState(false);
    let router = undefined;


    useEffect(() => {
        const check_access_token = async () => {
            if (hasMounted) {
                const _token = window.localStorage.getItem("token");
                const response = await API_CALLS.isAuthenticated(_token);
                console.log("response expenses: ", response);
                if (response.statue_code !== 200) {
                    router.push("/account");
                } else {
                    console.log("Authentication successful!");
                }
            }
        }
        check_access_token();

        Promise.all([
            API_CALLS.SELECT("expense", undefined, undefined, 3104),
            API_CALLS.SELECT("bank", undefined, undefined, 3104),
            API_CALLS.SELECT("category", undefined, undefined, 3104),
        ]).then(([resExpense, resBank, resCategory]) => 
            Promise.all([resExpense.data, resBank.data, resCategory.data])
        ).then(([dataExpense, dataBank, dataCategory]) => {
            setExpenses(dataExpense);
            setBanks(dataBank);
            setCategories(dataCategory);
            setTotal((prevState) => dataExpense.reduce((accumelator, currentValue) => {
                    return accumelator + ((currentValue.expense_type == "Expense" ? -1 : 1) * currentValue.expense_amount);
                }, 0)
            );
        });
        setHasMounted(true);
    }, [hasMounted]);

    const submit_item = async (type, item) => {
        const item_response = await API_CALLS.INSERT(type, undefined, undefined, item, 3104);
    }


    if (!hasMounted) {
        return null;
    } else {
        router = useRouter();
    }

    return (
        <div className="expense_scene">
            <div className="expense_left_side">
                <div className="search_bar">
                    <input type="text" placeholder="Search by service, date or category" />
                </div>
                <div className="transactions">
                    <div className="expenses_title">
                        <div>Transactions</div>
                        <div>{constant.formatter(total)}</div>
                    </div>
                    <div className="expenses_items">
                        {expenses.map((item, index) => <ExpenseItem key={index} item={item} />)}
                    </div>
                </div>
            </div>
            <div className="expense_middle_side">
                <div className="sticky_item">
                    <div className="cards_accounts_title">
                        <div>Accounts</div>
                        <div onClick={() => setState((prevState) => !prevState)}>
                            <FontAwesomeIcon icon={state ? faMinus : faPlus} style={{ fontSize: 24, color: "#fff" }} />
                        </div>
                    </div>
                    <NewBank newState={{ state, setState }} submit_item={submit_item} />
                </div>
                { banks.map((bank, index) => <CreditCard key={index} bank={bank} /> )}
            </div>
            <div className="expense_right_side">
                <div className="new_expense_title">New Transaction</div>
                <ExpenseNewItem category={category} submit_item={submit_item} />
            </div>
        </div>
    )
}