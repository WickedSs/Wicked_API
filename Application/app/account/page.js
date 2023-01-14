import Image from 'next/image'
import '../../styles/Login.css'
import upgradePng from '../../icons/up-arrow.png'
import Form from '../../components/Login/login_form';




export default function Login() {

    return (
        <main className="login">
            <div className="top_side">
                <h3 className="logo_word">Upgrade</h3>
            </div>
            <div className="middle_side">
                <Form />
                <div className="right_side">
                    <Image alt="Upgrade Logo" src={upgradePng} width={512} height={512} />
                </div>
            </div>
        </main>
    )
} 