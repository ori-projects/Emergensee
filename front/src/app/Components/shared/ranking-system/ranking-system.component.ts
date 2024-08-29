import { Component, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-ranking-modal',
  template: `
    <h2 mat-dialog-title>Ranking System</h2>
    <div mat-dialog-content>
      <h3>Please rate from 0 to 5 according to relevance of the following:</h3>
      <p>Current critical disease level </p>
      <input type="number" min="0" max="5" [(ngModel)]="diseaseRating">
      
      <p>Current chronic kidney disease</p>
      <input type="number" min="0" max="5" [(ngModel)]="ckdRating">
      
      <p>Predict new infections</p>
      <input type="number" min="0" max="5" [(ngModel)]="sirRating">
      
      <p>Current maternal health</p>
      <input type="number" min="0" max="5" [(ngModel)]="maRating">
      
      <div *ngIf="showErrorMessage" style="color: red;">Please enter values greater than 0 for at least one rating.</div>
    </div>
    <div mat-dialog-actions>
      <button mat-button (click)="onClose()">Save</button>
    </div>
  `,
  styleUrls: ['./ranking-system.component.css']
})
export class RankingModalComponent {
  diseaseRating: number = 1;
  ckdRating: number = 1;
  sirRating: number = 1;
  maRating: number = 1;
  showErrorMessage: boolean = false;

  constructor(
    public dialogRef: MatDialogRef<RankingModalComponent>, // Inject MatDialogRef
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {}

  onClose() {
    if (this.diseaseRating === 0 && this.ckdRating === 0 && this.sirRating === 0 && this.maRating === 0) {
      this.showErrorMessage = true;
    } else {
      this.showErrorMessage = false;
      // Only close the modal if at least one rating is greater than 0
      if (this.diseaseRating > 0 || this.ckdRating > 0 || this.sirRating > 0 || this.maRating > 0) {
        this.dialogRef.close({
          diseaseRating: this.diseaseRating,
          ckdRating: this.ckdRating,
          sirRating: this.sirRating,
          maRating: this.maRating
        });
      }
    }
  }
}