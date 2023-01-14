import constant from "../../constants";
import { useEffect, useState } from "react";

export default function Bank({ bank }) {

    const [indexColor, setIndexColor] = useState(0);
    const [colors] = useState({
        background: {
            top: ["#F5DDC8", "#E4D7F2", "#E4EDE9"],
            bottom: ["#E9AD79", "#A785C5", "#85B998"]
        },
        upper: ["#64574F", "#645A72", "#686E70"],
        middle: [
            { left: "#6F5F55", right: "#21232E" },
            { left: "#7C728A", right: "#252534" },
            { left: "#686E70", right: "#1C282C" },
        ],
        bottom: [
            { left: "#212121", right: "#36220F" },
            { left: "#fff", right: "#1A0E22" },
            { left: "#212121", right: "#0E261B" },
        ]
    });

    useEffect(() => {
        const pick_color_index = () => {
            const index = constant.getRandomNumberBetween(0, 2);
            setIndexColor(index);
        }
        pick_color_index();
    }, [bank]);

    const bank_card_number = "**** ".repeat(3) + bank?.bank_card_number.slice(-4);

    return (
        <div className="credit_card">
            <div className="upper_details" style={{ background: colors.background.top[indexColor] }}>
                <div style={{ fontSize: "1.3em", color: colors.upper[indexColor] }}>{bank?.bank_name}</div>
                <div style={{ fontSize: "1.3em", fontWeight: "normal", color: colors.upper[indexColor] }}>{constant.formatter(bank?.bank_amount)}</div>
                {/* <FontAwesomeIcon icon={faCreditCardAlt} style={{ fontSize: 24, color: colors.upper[indexColor] }} /> */}
            </div>
            <div className="middle_details" style={{ background: colors.background.top[indexColor] }}>
                <div style={{ fontSize: "1em", color: colors.middle[indexColor].left }}>{bank?.bank_holder_name || "Souleymane Guerida"}</div>
                <div style={{ fontSize: "1em", color: colors.middle[indexColor].right }}>{bank_card_number || "*** **** **** 2546"}</div>
            </div>
            <div className="bottom_details" style={{ background: colors.background.bottom[indexColor] }}>
                <div style={{ fontSize: "1em", color: colors.bottom[indexColor].left }}>{bank?.bank_bank_number || "07999954987785"}</div>
                <div style={{ fontSize: "1em", color: colors.bottom[indexColor].right }}>{bank?.bank_card_type || "Algerie Poste"}</div>
            </div>
        </div>
    )
}