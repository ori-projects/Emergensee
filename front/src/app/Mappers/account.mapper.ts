import { Account } from "../Modules/account/accountModule";

export class AccountMapper {
    static mapToAccount(data: any[]): Account {
        if (data.length !== 5) {
            return null;
        }

        return {
            id: data[0],
            name: data[2],
            email: data[1],
            password: data[3],
            role: data[4],
        };
    }
}
