import { Component, Input } from '@angular/core';
import { MlmodelModule } from '../../../../Modules/mlmodel/mlmodel.module';

@Component({
  selector: 'app-mlmodel-detail',
  templateUrl: './mlmodel-detail.component.html',
  styleUrls: ['./mlmodel-detail.component.css']
})
export class MlmodelDetailComponent {
  @Input() selectedModel: MlmodelModule;
}
