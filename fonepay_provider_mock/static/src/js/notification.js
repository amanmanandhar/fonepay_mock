/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class FonepayTestButton extends Component{
    static template = 'fonepay_provider_mock.FonepayTestButtonView'
    setup(){
        this.orm = useService("orm");
        this.notification = useService('notification');
    }
    async onClick(){
        const result = await this.orm.call(
            "payment.provider",
            "fonepay_test_connection",
            [[this.props.record.resId]]
        );
        if (result.success) {
            this.notification.add(result.message, {
                type: "success",
            })
        } else {
            this.notification.add(result.message, {
                type: "danger",
            })
        }
    }
}
registry.category('fields').add('fonepay_test_button', FonepayTestButton)