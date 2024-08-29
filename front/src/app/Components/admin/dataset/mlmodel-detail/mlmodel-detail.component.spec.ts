import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MlmodelDetailComponent } from './mlmodel-detail.component';

describe('MlmodelDetailComponent', () => {
  let component: MlmodelDetailComponent;
  let fixture: ComponentFixture<MlmodelDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [MlmodelDetailComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(MlmodelDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
