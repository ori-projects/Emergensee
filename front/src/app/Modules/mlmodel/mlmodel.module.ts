// mlmodel.model.ts
export class MlmodelModule {
  constructor(
    public labeled: boolean,
    public name: string,
    public description: string
  ) {}
}