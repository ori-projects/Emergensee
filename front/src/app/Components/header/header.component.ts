import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../Services/auth.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  isDropdownOpen: boolean = false;
  id: number = null;
  name: string = '';
  role: number = 0;

  constructor(private router: Router, private authService: AuthService) {
    this.authService.userState$.subscribe(user => {
      if (user) {
        this.id = user.id;
        this.name = user.name;
        this.role = user.role;
      } else {
        this.id = null;
        this.name = '';
        this.role = 0;
      }
    });
  }

  isLoginPage(): boolean {
    return this.router.url === '/login';
  }

  logout() {
    this.toggleDropdown();
    this.authService.logout();
    this.router.navigate(['/login']);
  }

  toggleDropdown() {
    this.isDropdownOpen = !this.isDropdownOpen;
  }

  showAdminPage(): boolean {
    return this.role === 2;
  }

  showDoctorPage(): boolean {
    return this.role === 1;
  }
}