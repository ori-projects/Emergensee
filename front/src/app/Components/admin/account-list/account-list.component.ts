import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Account } from '../../../Modules/account/accountModule';
import { ApiService } from '../../../Services/api.service';
import { AccountMapper } from '../../../Mappers/account.mapper';
import { AuthService } from '../../../Services/auth.service';

@Component({
  selector: 'app-account-list',
  templateUrl: './account-list.component.html',
  styleUrls: ['./account-list.component.css']
})
export class AccountListComponent implements OnInit {
  accounts: Account[] = [];
  selectedAccount: Account | null = null;
  showNewAccountForm = false;
  accountForm = new FormGroup({
    email: new FormControl('', [Validators.required, Validators.email]),
    username: new FormControl('', [Validators.required, Validators.minLength(3)]),
    password: new FormControl('', [Validators.required, Validators.minLength(6)]),
    role: new FormControl('admin', Validators.required)
  });

  // Confirmation dialog control
  confirmDelete = false;

  constructor(private apiService: ApiService, private authService: AuthService) { }

  ngOnInit() {
    this.loadAccounts();
  }

  loadAccounts() {
    this.apiService.getAccounts(this.authService.getId()).subscribe(
      (response) => {
        if (response && response.accounts) {
          this.accounts = response.accounts.map(dataArray => AccountMapper.mapToAccount(dataArray));
        } else {
          console.error('Invalid response format:', response);
        }
      },
      error => {
        console.error('Error loading accounts:', error);
      }
    );
  }

  onAccountSelect(account: Account) {
    this.selectedAccount = account;
  }

  // Show confirmation dialog
  showConfirmationDialog(account: Account) {
    this.selectedAccount = account;
    this.confirmDelete = true;
  }

  // Confirm deletion action
  confirmDeleteAction(account: Account) {
    this.apiService.deleteAccount(account).subscribe(
      () => {
        const index = this.accounts.indexOf(account);
        if (index !== -1) {
          this.accounts.splice(index, 1);
        }
        this.confirmDelete = false; // Close confirmation dialog
      },
      error => {
        console.error('Error removing account:', error);
        this.confirmDelete = false; // Close confirmation dialog on error too
      }
    );
  }

  createAccount() {
    if (this.accountForm.valid) {
      const newAccount = this.accountForm.value;
      this.apiService.createAccount(newAccount).subscribe(
        (response) => {
          // Assuming response contains newly created account details
          const createdAccount = response.account;
          this.accounts.push(createdAccount); // Add new account to list
          this.showNewAccountForm = false; // Hide form after successful creation
          this.accountForm.reset(); // Reset form
        },
        (error) => {
          console.error('Error creating account:', error);
          // Handle error here, show error message or retry logic
        }
      );
    } else {
      // Form is invalid, do not submit
      console.error('Form is invalid. Cannot submit.');
    }
  }

  // Cancel deletion action
  cancelDelete() {
    this.selectedAccount = null;
    this.confirmDelete = false;
  }

  toggleNewAccountForm() {
    this.showNewAccountForm = !this.showNewAccountForm;
    this.accountForm.reset();
  }
}