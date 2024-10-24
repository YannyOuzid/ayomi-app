import React from "react";
import "./CalculatorHead.css"

const CalculatorHead = (props) => {

    return (
        <div className="calculator-head">
            <div className="result-display">
                {props.data && props.data.map((item) => {
                    return (<>
                        <p>
                            {item.toString()}
                        </p>
                    </>
                    )
                })}
            </div>
        </div>
    )

}

export default CalculatorHead;