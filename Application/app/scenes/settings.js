import { createRef, useState } from "react"

import AccountSettings from "../../components/Settings/accounts_settings"
import ProductSettings from "../../components/Settings/products_settings"

import '../../styles/settings.css';

export default function Settings() {

    return (
        <div className="setting_scene">
            <ProductSettings />
            <AccountSettings />
        </div>
    )
}