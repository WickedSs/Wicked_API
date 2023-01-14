import { createRef, useState, useEffect } from "react"
import constant from "../../constants"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPen } from "@fortawesome/free-solid-svg-icons";
import API_CALLS from "../../app/api/api_routes";



function TableHead({}) {
    return (
        <div className="table account">
            <table className="table_head">
                <thead>
                    <tr className="thead_tr_header">
                        <th>
                            <label>Username</label>
                        </th>
                        <th>
                            <label>Fullname</label>
                        </th>
                        <th>
                            <label>Monthly Expenses</label>
                        </th>
                        <th>
                            <label>Type</label>
                        </th>
                        <th>
                            <label>Monthly Salary</label>
                        </th>
                        <th>
                            <label>Started At</label>
                        </th>
                        <th>
                            <label></label>
                        </th>
                    </tr>
                </thead>
            </table>
        </div>
    )
}

function TableNewItem({}) {

    const user_name = createRef(), user_fullname = createRef(), user_password = createRef(), user_type = createRef();
    const user_role = createRef(), user_key = createRef();
    const [accountItem, setAccountItem] = useState({
        id: 0,
        user_name: undefined,
        user_fullname: undefined,
        user_password: undefined,
        user_type: undefined,
        user_role: undefined,
        user_key: undefined,
    });

    return (
        <div className="table new_item">
            <table className="table_fix_item">
                <tbody>
                    <tr className="thead_tr_header">
                        <th>
                            <input name="username" type="text" id="usernameInput" placeholder="..." 
                                ref={user_name} value={accountItem?.user_name || ""}
                                onChange={(e) => setAccountItem((prevState) => ({ ...prevState, user_name: e.target.value }))}
                            />
                        </th>
                        <th>
                            <input name="user_fullname" type="text" id="user_fullnameInput" placeholder="..." 
                                ref={user_fullname} value={accountItem?.user_fullname || ""}
                                onChange={(e) => setAccountItem((prevState) => ({ ...prevState, user_fullname: e.target.value }))}
                            />
                        </th>
                        <th>
                            <input name="user_password" type="password" id="user_passwordInput" placeholder="..." 
                                ref={user_password} value={accountItem?.user_password || ""}
                                onChange={(e) => setAccountItem((prevState) => ({ ...prevState, user_password: e.target.value }))}
                            />
                        </th>
                        <th>
                            <input name="user_type" type="text" id="user_typeInput" placeholder="..." 
                                ref={user_type} value={accountItem?.user_type || ""}
                                onChange={(e) => setAccountItem((prevState) => ({ ...prevState, user_type: e.target.value }))}
                            />
                        </th>
                        <th>
                            <input name="monthly_salary" type="text" id="monthly_salaryInput" placeholder="...."
                                ref={user_key} value={accountItem?.user_key || ""}
                                onChange={(e) => setAccountItem((prevState) => ({ ...prevState, monthly_salary: e.target.value }))}
                            />
                        </th>
                        <th>
                            <input name="off_stock_min" type="text" id="off_stock_minInput" placeholder="User Key"
                                ref={user_key} value={constant.getCurrentDate()}
                                onChange={(e) => setAccountItem((prevState) => ({ ...prevState, started_at: e.target.value }))}
                            />
                        </th>
                        <th>
                            <label>Append</label>
                        </th>
                    </tr>
                </tbody>
            </table>
        </div>
    )
}

function TableItem({ account, employee }) {

    const [itemAccount, setItemAccount] = useState({
        user_name: account?.user_name || "",
        user_fullname: account?.user_fullname || "",
        user_password: "",
        user_type: account?.user_type || "",
        user_role: account?.user_role || "",
        user_key: account?.user_key || "",
    });

    const [itemEmployee, setItemEmployee] = useState({
        fullname: employee?.fullname || "",
        started_at: employee?.started_at || "",
        stopped_at: employee?.stopped_at || "",
        employee_key: employee?.employee_key || "",
        monthly_salary: employee?.monthly_salary || 0,
        birthday: employee?.birthday || "",
        monthly_expenses: employee?.monthly_expenses || 0,
        phone_number: employee?.phone_number || "",
        avatar: employee?.avatar || "",
    });

    return (
        <div className="table item">
            <table className="table_item">
                <tbody>
                    <tr className="tbody_tr_item">
                        <th>
                            <input name="username" type="text" id="usernameInput" value={itemAccount?.user_name || ""}
                                onChange={(e) => setItemAccount((prevState) => ({ ...prevState, user_name: e.target.value }))}
                            />
                        </th>
                        <th>
                            <input name="user_fullname" type="text" id="user_fullnameInput" value={itemEmployee?.fullname || ""}
                                onChange={(e) => setItemEmployee((prevState) => ({ ...prevState, fullname: e.target.value }))}
                            />
                        </th>
                        <th>
                            <input name="monthly_expenses" type="text" id="monthly_expensesInput" value={constant.formatter(itemEmployee?.monthly_expenses)} 
                                disabled={true}
                                onChange={(e) => setItemEmployee((prevState) => ({ ...prevState, monthly_expenses: e.target.value }))}
                            />
                        </th>
                        <th>
                            <input name="user_type" type="text" id="user_typeInput" value={itemAccount?.user_type || ""}
                                disabled={true}
                                onChange={(e) => setItemAccount((prevState) => ({ ...prevState, user_type: e.target.value }))}
                            />
                        </th>
                        <th>
                            <input name="monthly_salary" type="text" id="monthly_salaryInput" value={constant.formatter(itemEmployee?.monthly_salary || 25000)}
                                onChange={(e) => setItemEmployee((prevState) => ({ ...prevState, monthly_salary: e.target.value }))}
                            />
                        </th>
                        <th>
                            <input name="monthly_salary" type="text" id="monthly_salaryInput" 
                                value={itemEmployee?.started_at.length > 0 ? itemEmployee?.started_at : itemEmployee?.stopped_at}
                                onChange={(e) => setItemEmployee((prevState) => ({ ...prevState, monthly_salary: e.target.value }))}
                            />
                        </th>
                        <th>
                            <label>Update</label>
                        </th>
                    </tr>
                </tbody>
            </table>
        </div>
    )
}

export default function AccountSettings({}) {

    const [accounts, setAccounts] = useState([]);
    const [employees, setEmployees] = useState([]);

    useEffect(() => {
        Promise.all([
            API_CALLS.SELECT("user", undefined, undefined, 3105),
            API_CALLS.SELECT("employee", undefined, undefined, 3106),
        ]).then(([resAccount, resEmployee]) => 
            Promise.all([resAccount.data, resEmployee.data])
        ).then(([dataAccount, dataEmployee]) => {
            setAccounts(dataAccount);
            setEmployees(dataEmployee);
        });
    }, []);

    return (
        <div>
            <div className="account_detail_settings">
                <div className="account_detail_title">Accounts & Employees</div>
                <TableHead />
                <TableNewItem />
                {
                    accounts.map((account, index) => {
                        let employee = employees.find(item => item.user_key == account.employee_key);
                        return <TableItem account={account} employee={employee} />
                    })
                }
            </div>
        </div>
    )
}