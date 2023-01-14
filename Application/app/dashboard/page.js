import Head from 'next/head'
import Image from 'next/image'
import Router from 'next/router'
import { setCookie, getCookie } from 'cookies-next';
import { useEffect, useState } from 'react'

import Sellings from '../scenes/sellings';
import Products from '../scenes/products';
import Expenses from '../scenes/expenses';
import Invoices from '../scenes/invoices';
import Settings from '../scenes/settings';
import Login from '../account/page';


export default function Dashboard({ _current_trade_registry }) {

    const [selectedScene, setSelectedScene] = useState(0);
    const [currentTradeRegistry, setCurrentTradeRegistry] = useState(1);
    const [jsonToken, setJsonToken] = useState(undefined);

    function parseJwt(token) {
        if (!token) { return; }
        const base64Url = token.split('.')[1];
        const base64 = base64Url.replace('-', '+').replace('_', '/');
        return JSON.parse(window.atob(base64));
    }

    const scenes = [
        { index : 0, scene: <Sellings _currentTradeRegistry={currentTradeRegistry} />, role: "Admin, Employee", scope: "Basic" },
        { index : 1, scene: <Products />, role: "Admin, Employee", scope: "Basic" },
        { index : 2, scene: <Expenses />, role: "Admin, Employee", scope: "Basic"  },
        { index : 3, scene: <Invoices _currentTradeRegistry={currentTradeRegistry} />, role: "Admin, Employee", scope: "Basic"  },
        { index : 4, scene: <Settings />, role: "Admin", scope: "Basic"  },
    ];  

    useEffect(() => {
        const check_token = () => {
            const token = getCookie('access_token');
            if (token !== undefined) {
                setJsonToken(parseJwt(token));
            } else {
                setJsonToken(undefined);
            }
        }
        check_token();
    }, []);

    if (jsonToken == undefined) {
        Router.replace("/account/login");
    }

    return (
        <div className="dashboard">
            <Navigation _selectScene={{ selectedScene, setSelectedScene }} _tradeRegistry={{ currentTradeRegistry, setCurrentTradeRegistry }} jsonToken={jsonToken} />
            { scenes[selectedScene].role.split(",").includes(jsonToken.role) && jsonToken.scope === scenes[selectedScene].scope ? scenes[selectedScene].scene : null }
        </div>
    )
}