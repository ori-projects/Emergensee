import { ComponentFixture, TestBed } from '@angular/core/testing';

import { datasetComponent } from './dataset.component';

describe('datasetComponent', () => {
  let component: datasetComponent;
  let fixture: ComponentFixture<datasetComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [datasetComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(datasetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
