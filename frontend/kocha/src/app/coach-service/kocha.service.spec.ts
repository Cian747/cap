import { TestBed } from '@angular/core/testing';

import { KochaService } from './kocha.service';

describe('KochaService', () => {
  let service: KochaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(KochaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
