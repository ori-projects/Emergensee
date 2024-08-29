import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../Services/auth.service';
import { AccountMapper } from '../../Mappers/account.mapper';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private router: Router, private authService: AuthService) {}

  login(loginForm: any): void {
    if (loginForm.valid) {
      const formData = { email: this.email, password: this.password };
      this.authService.login(formData).subscribe(
        response => {
          if (response && response.success) {
            const account = AccountMapper.mapToAccount(response.account);
            this.authService.setUser(account); // Set the user in AuthService
            if (account.role === 1) {
              this.router.navigate(['/patients']);
            } else if (account.role === 2) {
              this.router.navigate(['/dashboard']);
            } else {
              this.errorMessage = 'Invalid role';
            }
          } else {
            this.errorMessage = 'Invalid credentials';
          }
        },
        error => {
          console.error(error);
          this.errorMessage = 'An error occurred while processing your request.';
        }
      );
    } else {
      this.errorMessage = 'Please correct the errors in the form.';
    }
  }
}