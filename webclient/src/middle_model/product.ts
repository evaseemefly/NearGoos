class SearchCondition {
  cateogry: string;
  area: string;
  period: string;
  start: Date;
  end: Date;
  constructor(
    type: string,
    area: string,
    period: string,
    start: Date,
    end: Date,
  ) {
    this.cateogry = type;
    this.area = area;
    this.period = period;
    this.start = start;
    this.end = end;
  }
}

// tslint:disable-next-line: max-classes-per-file
class ProductImageCondition {
  cateogry: string;
  area: string;
  period: string;
  constructor(
    cateogry: string,
    area: string,
    period: string,
  ) {
    this.cateogry = cateogry;
    this.area = area;
    this.period = period;
  }
}

export { SearchCondition, ProductImageCondition };
