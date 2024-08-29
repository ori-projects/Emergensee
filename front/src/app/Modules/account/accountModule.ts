export class Account {
    id: number;
    name: string;
    email: string;
    password: string;
    role: number;
  
    constructor(id: number, name: string, email: string, password: string, role: number) {
      this.id = id;
      this.name = name;
      this.email = email;
      this.password = password;
      this.role = role;
    }
  }
  