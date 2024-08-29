// decision-dataset.model.ts
import { MlmodelModule } from "../mlmodel/mlmodel.module";

export class Decisiondataset {
  constructor(
    public name: string,
    public numberOfLines: number,
    public relativeWeight: number,
    public mlmodels: MlmodelModule[]
  ) {}
}