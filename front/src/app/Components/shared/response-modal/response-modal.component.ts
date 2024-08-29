import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-response-modal',
  template: `
    <h2 mat-dialog-title>Final risk assessment</h2>
    <div mat-dialog-content>
      <p>Detailed risk assessment:</p>
      <p class="final-assessment">{{ data.finalAssessment }}</p>
      <button *ngIf="!showComponents" mat-button style="background-color: #ccc; color: #fff;" (click)="toggleComponents()">Components</button>
      <div *ngIf="showComponents">
        <br/>
        <p>Calculated according to the following components:</p>
        <p *ngFor="let line of data.components" [ngClass]="getRiskColor(line)">{{ line }}</p>
      </div>
    </div>
    <div mat-dialog-actions>
      <button mat-button [mat-dialog-close]="true">Close</button>
    </div>
  `,
  styleUrls: ['./response-modal.component.css']
})
export class ResponseModalComponent {
  showComponents = false;
  buttonClicked = false;

  constructor(@Inject(MAT_DIALOG_DATA) public data: { finalAssessment: string, components: string[] }) {}

  toggleComponents() {
    this.showComponents = !this.showComponents;
    this.buttonClicked = true; // Set buttonClicked to true on first toggle
  }

  getRiskColor(line: string): string {
    if (!line) return ''; // Handle null or undefined lines gracefully

    const percentage = this.extractPercentage(line);
    if (percentage >= 0 && percentage <= 34) {
      return 'text-success'; // Bootstrap class for green text
    } else if (percentage >= 35 && percentage <= 66) {
      return 'text-warning'; // Bootstrap class for orange text
    } else if (percentage >= 67 && percentage <= 100) {
      return 'text-danger'; // Bootstrap class for red text
    } else {
      return ''; // Default or error case
    }
  }

  private extractPercentage(line: string): number {
    const match = line.match(/(\d+(\.\d+)?)%/);
    if (match) {
      return parseFloat(match[1]);
    }
    return -1; // Default or error case
  }
}