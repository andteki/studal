import { TestBed } from '@angular/core/testing';

import { ApiclassService } from './apiclass.service';

describe('ApiclassService', () => {
  let service: ApiclassService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ApiclassService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
