import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DecisiondatasetListComponent } from './decision-dataset-list.component';

describe('DecisiondatasetListComponent', () => {
  let component: DecisiondatasetListComponent;
  let fixture: ComponentFixture<DecisiondatasetListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [DecisiondatasetListComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DecisiondatasetListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
