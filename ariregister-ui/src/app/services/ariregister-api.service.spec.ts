import { TestBed } from '@angular/core/testing';

import { AriregisterApiService } from './ariregister-api.service';

describe('AriregisterApiService', () => {
  let service: AriregisterApiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AriregisterApiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
