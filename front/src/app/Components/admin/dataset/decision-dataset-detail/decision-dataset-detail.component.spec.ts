import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DecisiondatasetDetailComponent } from './decision-dataset-detail.component';

describe('DecisiondatasetDetailComponent', () => {
  let component: DecisiondatasetDetailComponent;
  let fixture: ComponentFixture<DecisiondatasetDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [DecisiondatasetDetailComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DecisiondatasetDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
